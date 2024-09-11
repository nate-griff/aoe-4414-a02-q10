# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#   Converts Latitude, Longitude, and Height (LLH) coordinates to ECEF coordinates.
# Parameters:
#  lat_deg: latitude in degrees
#  lon_deg: longitude in degrees
#  hae_km: height above ellipsoid in km
# Output:
#  Print the ECEF coordinates
#
# Written by Nathan Griffin
# Other contributors: GitHub Copilot
#
# See the LICENSE file for the license.

# import Python modules
import math
import sys

# Constants
R_E_KM = 6378.1363  # Earth's equatorial radius in km
E_E = 0.081819221456  # Earth's eccentricity

def llh_to_ecef(lat, lon, h):
    """
    Convert Latitude, Longitude, and Height (LLH) to ECEF coordinates.
    """
    # Convert latitude and longitude from degrees to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Calculate the prime vertical radius of curvature
    CE = R_E_KM / math.sqrt(1 - E_E**2 * math.sin(lat_rad)**2)
    SE = R_E_KM * (1 - E_E**2) / math.sqrt(1 - E_E**2 * math.sin(lat_rad)**2)

    # Calculate ECEF coordinates
    x_ecef = (CE + h) * math.cos(lat_rad) * math.cos(lon_rad)
    y_ecef = (CE + h) * math.cos(lat_rad) * math.sin(lon_rad)
    z_ecef = (SE + h) * math.sin(lat_rad)

    return x_ecef, y_ecef, z_ecef

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 llh_to_ecef.py lat_deg lon_Deg hae_km")
        sys.exit(1)

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])
    h = float(sys.argv[3])

    x_ecef, y_ecef, z_ecef = llh_to_ecef(lat, lon, h)

    print(f"{x_ecef:.6f}")
    print(f"{y_ecef:.6f}")
    print(f"{z_ecef:.6f}")

if __name__ == "__main__":
    main()
