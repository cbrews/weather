import {useEffect, useState} from 'react'
import {getLocationDetails} from './api';

interface CityDetailsProps {
    id: number
}

interface WeatherDetails {
    id: number
    name: string
}

export default function CityDetails({id}: CityDetailsProps) {
    const [weatherDetails, setWeatherDetails] = useState<WeatherDetails | undefined>(undefined)
    useEffect(() => {
        getLocationDetails(id)
            .then((res: any) => setWeatherDetails(res))
    })

    return <>{JSON.stringify(weatherDetails)}</>
}