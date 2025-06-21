LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (22.9734, 78.6569),  # Center of India
    'DEFAULT_ZOOM': 5,
    'MIN_ZOOM': 4,
    'MAX_ZOOM': 18,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'India Map',
    'TILES': [
        ('OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            'attribution': '&copy; OpenStreetMap contributors',
            'detectRetina': True,
            'maxNativeZoom': 18,
            'maxZoom': 22
        }),
        ('CartoDB Positron', 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
            'attribution': '&copy; CartoDB, OSM',
            'detectRetina': True,
            'maxNativeZoom': 18,
            'maxZoom': 22
        }),
    ]
}
