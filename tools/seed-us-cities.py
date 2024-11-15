from datetime import date, timedelta
from random import randrange

import httpx
from dotenv import load_dotenv
from pydantic import ValidationError
from typer import Typer, echo

from app.db import session
from app.models.location import Location
from app.models.measurement import Measurement

cli = Typer()

URL = "https://raw.githubusercontent.com/lutangar/cities.json/refs/heads/master/cities.json"


@cli.command()
def seed() -> None:
    load_dotenv(".env")

    echo(f"Loading cities from {URL}...")
    response = httpx.get(URL)
    cities = response.json()

    with session() as sess:
        i = 0
        for city in cities:
            if city.get("country", None) == "US":
                try:
                    location = Location(
                        city=city.get("name", None),
                        state=city.get("admin1", None),
                        country="US",
                        lat=city.get("lat", None),
                        long=city.get("lng", None),
                    )

                    location.model_validate(location)

                    sess.add(location)
                    sess.flush()

                    for i in range(0, 6):
                        temp_avg_c = randrange(17, 30)

                        assert location.id is not None
                        measurement = Measurement(
                            location_id=location.id,
                            date=date.today() - timedelta(days=i),
                            temp_avg=temp_avg_c,
                            temp_low=temp_avg_c - randrange(0, 5),
                            temp_high=temp_avg_c + randrange(0, 5),
                        )
                        sess.add(measurement)

                    sess.commit()
                    i += 1
                except ValidationError as e:
                    echo(f"Problem parsing data, skipping city {city}: {str(e)}")
                except Exception as e:
                    sess.rollback()
                    if "duplicate key value violates unique constraint" in str(e):
                        echo(f"Duplicate record, skipping city {city}: {str(e)}")
                    else:
                        raise e

        echo(f"Saved {i} cities to the database.")


if __name__ == "__main__":
    cli()
