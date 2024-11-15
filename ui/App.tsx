import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { useEffect, useState } from 'react';
import {getLocations} from './api';
import CityDetails from './CityDetails';
import {Location} from './types'


export default function App() {
    const [city, setCity] = useState<number | undefined>(undefined);
    const [cityList, setCityList] = useState<Location[]>([]);
    
    useEffect(() => {
        getLocations().then(locations => setCityList(locations))
    })

    return (
        <>
            <h1>Weather in{!!city ? ` ${city}` : "..."}</h1>
            <Autocomplete 
                options={cityList}
                renderInput={(params) => <TextField {...params} label="City" />}
                onChange={(_: any, newValue: Location | null) => {
                    setCity(newValue?.id);
                }}
            />
            {!!city && 
                <CityDetails id={city} />
            }
        </>
    )
}