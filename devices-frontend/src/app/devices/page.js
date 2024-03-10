// by default, components are server side components
// run command npm run dev to run server
import Link from 'next/link'


async function getDevices() {
    // endpoint points to django server
    const endpoint = 'http://localhost:8000/api/devices/'
    const res = await fetch(endpoint)

    if (!res.ok) {
        throw new Error('Failed to fetch data')
    }

    return res.json()
}


export default async function Devices() {
    const devices = await getDevices()

    // return GSX from component, which is essentially HTML
    return (
        <div className="flex flex-col items-center mt-s">
            <h1 className="test-4x1">My Devices</h1>

            {/* for each device (map), list them out */}
            <div className="mt-5 flex flex-col gap-2">
                { devices.map(device =>
                    <p className="text-xl text-blue-500 hover:text-blue-800" key={device.id}>
                    {/* reference the device-slug page */}
                        <Link href={`/devices/${device.slug}`}>
                            {device.name}
                        </Link>
                    </p>
                )}
            </div>
        </div>
    )
}