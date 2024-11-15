import useSWR from "swr";
import fetcher from "./api";
import { Location, Degrees } from "./types";
import Grid from "@mui/material/Grid2";

interface CityDetailsProps {
  location: Location;
  degrees: Degrees;
}

export default function CityDetails({ location, degrees }: CityDetailsProps) {
  const { data, error, isLoading } = useSWR(
    `/location/${location.id}/measurement/`,
    fetcher,
  );

  const degree_symbol = degrees == "celcius" ? "°C" : "°F";

  return (
    <Grid container spacing={2}>
      {!!data && [
        data.map((record: any) => (
          <Grid size={4}>
            <h2>{record.date}</h2>
            <p>
              Average: {record.temp_avg[degrees]} {degree_symbol}
            </p>
            <p>
              High: {record.temp_high[degrees]} {degree_symbol}
            </p>
            <p>
              Low: {record.temp_low[degrees]} {degree_symbol}
            </p>
          </Grid>
        )),
      ]}
    </Grid>
  );
}
