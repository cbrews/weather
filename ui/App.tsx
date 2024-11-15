import TextField from '@mui/material/TextField';
import {  MouseEvent} from 'react'
import Autocomplete, {AutocompleteInputChangeReason} from '@mui/material/Autocomplete';
import { useState , SyntheticEvent} from 'react';
import fetcher from './api';
import CityDetails from './CityDetails';
import {Location, Degrees} from './types'
import useSWR from 'swr'
import Container from '@mui/material/Container';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';


export default function App() {
    const [location, setLocation] = useState<Location | undefined>(undefined);
    const [userInput, setUserInput] = useState<string>("");
    const [degrees, setDegrees] = useState<Degrees>('celcius')
    const { data, error, isLoading } = useSWR(`/location/?search=${userInput}`, fetcher)

    let locations: Location[] = []
    if (!!data) {
        locations = (data as any[]).map((d: any) => ({id: d.id, name: `${d.city}, ${d.state}`} as Location));
    }

    return (
        <Container>
            <h1>Weather in{!!location?.name ? ` ${location.name}` : "..."}</h1>
            <Autocomplete 
                options={locations}
                disabled={!!error}
                getOptionLabel={(val) => val.name}
                loading={isLoading}
                value={location || null}
                onInputChange={(_:SyntheticEvent, value: string, reason: AutocompleteInputChangeReason) => {
                    if (reason == "input") {
                        setUserInput(value);
                    }
                }}
                renderInput={(params) => <TextField {...params} label="City" />}
                onChange={(_: SyntheticEvent, newValue: Location | null) => {
                    setLocation(newValue || undefined);
                }}
            />
            <ToggleButtonGroup
                value={degrees}
                exclusive
                onChange={(_: MouseEvent<HTMLElement>, value: Degrees) => {
                    if (value !== null) {
                        setDegrees(value)
                    }
                }}>
                <ToggleButton value="celcius" aria-label="left aligned">
                    °C
                </ToggleButton>
                <ToggleButton value="fahrenheit" aria-label="left aligned">
                    °F
                </ToggleButton>
            </ToggleButtonGroup>
            {!!location && 
                <CityDetails location={location} degrees={degrees} />
            }
        </Container>
    )
}