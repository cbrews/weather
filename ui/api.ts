import env from './env';
import {Location} from './types';

export async function getLocations(): Promise<Location[]> {
    const locations = await _get('/location/').then(res => res.json())
    return locations.map((l: any) => ({id: l.id, name: l.name}))
}

export async function getLocationDetails(id: number): Promise<Location> {
    const result = await _get(`/location/${id}/measurements/`)
    return {id: result.id, name: result.name}
}

async function _get(path: string): Promise<any> {
    const fullPath = env.baseUrl + path;
    const response = await fetch(fullPath, {mode: 'no-cors'});

    if (!response.ok) {
        throw new Error(`HTTP ERROR on ${fullPath} [${response.status}]`)
    }

    return await response.json();
}