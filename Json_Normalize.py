import json
import pandas as pd
from pandas import json_normalize

# Sample JSON data
data = {
    "locationDeliveries": [
        {
            "locationUniqueId": "L:ABC123",
            "locationNumber": "0004",
            "deliveries": [
                {
                    "fuelSystemName": "Regular 1-12",
                    "productClass": "ETHANOL_REGULAR",
                    "heightUOM": "INCHES",
                    "temperatureUOM": "CELSIUS",
                    "fuelSystemId": "04-b",
                    "tankActivities": [
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        },
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        }
                    ],
                    "startTime": "2021-05-20T19:38:01+00:00",
                    "endTime": "2021-05-20T19:48:01+00:00",
                    "deliveryVolumeGrossWithoutSales": 1234.5678,
                    "volumeUOM": "GALLONS",
                    "productCategory": "REGULAR",
                    "parentFuelSystemId": "04"
                },
                {
                    "fuelSystemName": "Regular 1-12",
                    "productClass": "ETHANOL_REGULAR",
                    "heightUOM": "INCHES",
                    "temperatureUOM": "CELSIUS",
                    "fuelSystemId": "04-b",
                    "tankActivities": [
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        },
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        }
                    ],
                    "startTime": "2021-05-20T19:38:01+00:00",
                    "endTime": "2021-05-20T19:48:01+00:00",
                    "deliveryVolumeGrossWithoutSales": 1234.5678,
                    "volumeUOM": "GALLONS",
                    "productCategory": "REGULAR",
                    "parentFuelSystemId": "04"
                }
            ]
        },
        {
            "locationUniqueId": "L:ABC123",
            "locationNumber": "0004",
            "deliveries": [
                {
                    "fuelSystemName": "Regular 1-12",
                    "productClass": "ETHANOL_REGULAR",
                    "heightUOM": "INCHES",
                    "temperatureUOM": "CELSIUS",
                    "fuelSystemId": "04-b",
                    "tankActivities": [
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        },
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        }
                    ],
                    "startTime": "2021-05-20T19:38:01+00:00",
                    "endTime": "2021-05-20T19:48:01+00:00",
                    "deliveryVolumeGrossWithoutSales": 1234.5678,
                    "volumeUOM": "GALLONS",
                    "productCategory": "REGULAR",
                    "parentFuelSystemId": "04"
                },
                {
                    "fuelSystemName": "Regular 1-12",
                    "productClass": "ETHANOL_REGULAR",
                    "heightUOM": "INCHES",
                    "temperatureUOM": "CELSIUS",
                    "fuelSystemId": "04-b",
                    "tankActivities": [
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        },
                        {
                            "endingHeight": 1234.5678,
                            "startingHeight": 1234.5678,
                            "endingTemperatures": [67.1234, 67.1234],
                            "endingWater": 1234.5678,
                            "startingVolumeGross": 1234.5678,
                            "tankUniqueId": "T:ABC123:TLS:V:3",
                            "startingWater": 1234.5678,
                            "startingTemperatures": [67.1234, 67.1234],
                            "endingVolumeGross": 1234.5678,
                            "probe": 3
                        }
                    ],
                    "startTime": "2021-05-20T19:38:01+00:00",
                    "endTime": "2021-05-20T19:48:01+00:00",
                    "deliveryVolumeGrossWithoutSales": 1234.5678,
                    "volumeUOM": "GALLONS",
                    "productCategory": "REGULAR",
                    "parentFuelSystemId": "04"
                }
            ]
        }
    ],
    "companyId": "companyId",
    "truncated": True,
    "continuationToken": "continuationToken"
}

# Flattening the JSON data
location_deliveries = data["locationDeliveries"]
flat_data = []

for location in location_deliveries:
    location_info = {
        "locationUniqueId": location["locationUniqueId"],
        "locationNumber": location["locationNumber"]
    }
    for delivery in location["deliveries"]:
        delivery_info = {
            "fuelSystemName": delivery["fuelSystemName"],
            "productClass": delivery["productClass"],
            "heightUOM": delivery["heightUOM"],
            "temperatureUOM": delivery["temperatureUOM"],
            "fuelSystemId": delivery["fuelSystemId"],
            "startTime": delivery["startTime"],
            "endTime": delivery["endTime"],
            "deliveryVolumeGrossWithoutSales": delivery["deliveryVolumeGrossWithoutSales"],
            "volumeUOM": delivery["volumeUOM"],
            "productCategory": delivery["productCategory"],
            "parentFuelSystemId": delivery["parentFuelSystemId"]
        }
        for activity in delivery["tankActivities"]:
            activity_info = {
                "endingHeight": activity["endingHeight"],
                "startingHeight": activity["startingHeight"],
                "endingTemperatures": activity["endingTemperatures"],
                "endingWater": activity["endingWater"],
                "startingVolumeGross": activity["startingVolumeGross"],
                "tankUniqueId": activity["tankUniqueId"],
                "startingWater": activity["startingWater"],
                "startingTemperatures": activity["startingTemperatures"],
                "endingVolumeGross": activity["endingVolumeGross"],
                "probe": activity["probe"]
            }
            flat_data.append({**location_info, **delivery_info, **activity_info})

# Create DataFrame
df = pd.json_normalize(flat_data)

# Display DataFrame
print(df)

# Save to CSV (optional)
df.to_csv("flattened_data.csv", index=False)
