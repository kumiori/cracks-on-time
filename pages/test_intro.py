import streamlit as st
import json

marquee_css = """
<style>
.marquee-container {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    background-color: #f0f0f0;
    padding: 10px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.marquee-text {
    display: inline-block;
    animation: marquee 10s linear infinite;
    # font-size: 20px;
    color: #333;
    # font-family: Arial, sans-serif;
    font-weight: bold;
}

@keyframes marquee {
    from {
        transform: translateX(1%);
    }
    to {
        transform: translateX(-100%);
    }
}
</style>
"""

# The HTML structure for the marquee
marquee_html = """
<div class="marquee-container">
    <span class="marquee-text">
        🌍 Breaking: New insights into cryosphere crack mechanics unveiled! 🌌 
        Collaborations with IGE Grenoble are opening new horizons. 🧊 
        Exciting developments in ice fracture modeling and mapping! 🚀
    </span>
</div>
"""

st.markdown(
    "To explore real-time data and insights about cryosphere fractures around the globe. In occasion of the seminar at Institut des Géosciences de l'Environnement."
)

# Inject the custom marquee into the app
# st.markdown(marquee_css + marquee_html, unsafe_allow_html=True)

# Step 1: Greet the user and ask for their name
st.title("Why ice?")
st.markdown("Because ice cracks...")

st.title("We are mapping.")
# st.markdown("""
# We're excited to collaborate to explore and map the irreversible processes and behaviour of the cryosphere.
# Our aim is to create an interactive and collaborative platform to map knowledge and bridge its gaps, foster
# interdisciplinary connections, and deepen our understanding of ice behaviour.
# """)
name = st.text_input("`Nice to meet you, I’m...`")

if name:
    st.success(f"Wonderful to have you onboard, {name}.")

    st.markdown("### A Few Things to Know Before We Get Started:")
    st.markdown("""
    - **Purpose**: This initiative focuses on mapping knowledge about ice behavior, processes, and fracture phenomena, emphasizing scientific collaboration and interdisciplinary engagement.
    - **Your Role**: Your input will help create a shared knowledge map, identify gaps in understanding, and foster meaningful exchanges between researchers and practitioners.
    - **Privacy**: All shared data and responses are for collaborative research purposes only and will be handled with the utmost confidentiality.
    """)

    # Checkbox to acknowledge the terms
    agree = st.checkbox("Acknowledged", key="acknowledge")

    if agree:
        st.success("Great! Let's move forward and connect.")
    else:
        st.warning("Please acknowledge the guidelines to proceed.")

    if agree:
        """
Explanation of the Project’s Relevance:

### Why This Is Important:
###### Ice and cryospheric phenomena are complex and interconnected, spanning across disciplines like glaciology, mechanics, mathematics, and policy-making.

Mapping knowledge helps us to:
- Aggregate and organize scattered scientific knowledge.
- Identify underrepresented areas or gaps in research.
- Promote collaborative problem-solving approaches to critical challenges like ice sheet stability, sea-level rise, and cryosphere response to environmental change.    
"""

cryosphere_cracks = {
    "Ice Shelves (Antarctica)": [
        {
            "Region": "Ross Ice Shelf",
            "Latitude": -82.0,
            "Longitude": 175.0,
            "Elastic_Energy": 7,
            "Characteristics": {
                "Type": "Ice Shelf Crack",
                "Contributing Factors": [
                    "Ocean-induced basal melting",
                    "Surface melting and hydrofracturing",
                ],
                "Impact": "Potential loss of buttressing effect, accelerating glacier flow",
                "Significance": "Largest ice shelf in Antarctica, critical for sea-level stability",
            },
        },
        {
            "Region": "Ronne Ice Shelf",
            "Latitude": -78.5,
            "Longitude": -60.0,
            "Elastic_Energy": 6,
            "Characteristics": {
                "Type": "Ice Shelf Crack",
                "Contributing Factors": [
                    "Basal melting from warm water incursions",
                    "Surface crevassing under stress",
                ],
                "Impact": "Reduces ice shelf stability, influences ice sheet dynamics",
                "Significance": "Important buffer for ice flow into the Weddell Sea",
            },
        },
        {
            "Region": "Larsen C Ice Shelf",
            "Latitude": -67.5,
            "Longitude": -60.0,
            "Elastic_Energy": 8,
            "Characteristics": {
                "Type": "Ice Shelf Crack",
                "Contributing Factors": [
                    "Surface meltwater penetration and hydrofracturing",
                    "Rising atmospheric temperatures",
                    "Ice thinning due to atmospheric warming",
                    "Crack propagation driven by tides",
                ],
                "Impact": "Major ice shelf collapse events, increasing sea-level contribution",
                "Significance": "One of the most studied ice shelves due to collapse events",
            },
        },
        {
            "Region": "Amery Ice Shelf",
            "Latitude": -69.0,
            "Longitude": 70.0,
            "Elastic_Energy": 6,
            "Characteristics": {
                "Type": "Ice Shelf Crack",
                "Contributing Factors": [
                    "Tidal stresses and ocean-driven melting",
                    "Ice flow divergence near the grounding line",
                ],
                "Impact": "Significant for regional ice dynamics and ocean interactions",
                "Significance": "Third-largest ice shelf, important for East Antarctic stability",
            },
        },
    ],
    "Glaciers (Greenland & High Altitudes)": [
        {
            "Region": "Jakobshavn Glacier",
            "Latitude": 69.2,
            "Longitude": -49.8,
            "Elastic_Energy": 9,
            "Characteristics": {
                "Type": "Glacier Crack",
                "Contributing Factors": [
                    "High velocity of ice flow",
                    "Interaction with ocean water",
                ],
                "Impact": "Major contributor to Greenland ice mass loss",
                "Significance": "Fastest-flowing glacier, critical for global sea-level predictions",
            },
        },
        {
            "Region": "Helheim Glacier",
            "Latitude": 66.3,
            "Longitude": -38.1,
            "Elastic_Energy": 8,
            "Characteristics": {
                "Type": "Glacier Crack",
                "Contributing Factors": [
                    "Warm water penetration beneath the ice tongue",
                    "Rapid ice flow and basal stress",
                ],
                "Impact": "Increased calving and ice loss",
                "Significance": "Key glacier in Greenland ice sheet dynamics",
            },
        },
        {
            "Region": "Karakoram Glaciers",
            "Latitude": 35.0,
            "Longitude": 75.0,
            "Elastic_Energy": 7,
            "Characteristics": {
                "Type": "Glacier Crack",
                "Contributing Factors": [
                    "High altitude and steep gradients",
                    "Interaction between snow and ice melt",
                ],
                "Impact": "Local water resource fluctuations",
                "Significance": "Critical for regional hydrology and glacier-climate interactions",
            },
        },
    ],
    "Sea Ice (Arctic Ocean)": [
        {
            "Region": "Beaufort Sea",
            "Latitude": 73.0,
            "Longitude": -130.0,
            "Elastic_Energy": 4,
            "Characteristics": {
                "Type": "Sea Ice Crack",
                "Contributing Factors": [
                    "Wind-driven ice movement",
                    "Seasonal temperature fluctuations",
                ],
                "Impact": "Enhanced summer ice retreat and seasonal variability",
                "Significance": "Important for Arctic Ocean ice dynamics and albedo feedback",
            },
        },
        {
            "Region": "Laptev Sea",
            "Latitude": 75.0,
            "Longitude": 130.0,
            "Elastic_Energy": 3,
            "Characteristics": {
                "Type": "Sea Ice Crack",
                "Contributing Factors": [
                    "Seasonal ice formation and drift",
                    "Riverine heat input",
                ],
                "Impact": "Affects ice export through the Arctic Ocean",
                "Significance": "Key region for sea ice formation and Arctic circulation",
            },
        },
    ],
    "Permafrost Regions (Northern Hemisphere)": [
        {
            "Region": "Siberia",
            "Latitude": 65.0,
            "Longitude": 120.0,
            "Elastic_Energy": 5,
            "Characteristics": {
                "Type": "Permafrost Crack",
                "Contributing Factors": [
                    "Warming-induced thawing of permafrost",
                    "Formation of thermokarst features",
                ],
                "Impact": "Carbon release and landscape instability",
                "Significance": "Largest permafrost region, vital for carbon feedback mechanisms",
            },
        },
    ],
    "Subglacial Lakes and Basal Ice (Antarctica)": [
        {
            "Region": "Lake Vostok",
            "Latitude": -77.5,
            "Longitude": 106.8,
            "Elastic_Energy": 8,
            "Characteristics": {
                "Type": "Subglacial Crack",
                "Contributing Factors": [
                    "Pressurized water flow beneath ice",
                    "Interaction between basal ice and bedrock",
                ],
                "Impact": "Potential for subglacial lake outburst floods",
                "Significance": "Largest subglacial lake, crucial for understanding basal ice processes",
            },
        },
    ],
}


marquee_items = []
for category, regions in cryosphere_cracks.items():
    for region in regions:
        region_name = region["Region"]
        coordinates = (region["Latitude"], region["Longitude"])
        factors = " and ".join(region["Characteristics"]["Contributing Factors"])
        impact = region["Characteristics"]["Impact"]
        marquee_items.append(
            f"{region_name} {coordinates} [cracks by] {factors.lower()}, its impact: {impact.lower()}"
        )
pixels_per_second = 50  # Set a constant scrolling speed

marquee_text = " 🌍 ".join(marquee_items)
text_length_pixels = (
    len(marquee_text) * 10
)  # Approximate text length in pixels (adjust factor as needed)
animation_duration = text_length_pixels / pixels_per_second

# Create CSS with dynamic animation duration
marquee_css = f"""
<style>
.marquee-container {{
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    background-color: rgb(240, 242, 246);
    padding: 10px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    
}}

.marquee-text {{
    display: inline-block;
    animation: marquee {animation_duration}s linear infinite;
    font-size: 18px;
    color: #333;
    font-family: Arial, sans-serif;
    font-weight: bold;
}}

@keyframes marquee {{
    from {{
        transform: translateX(0%);
    }}
    to {{
        transform: translateX(-100%);
    }}
}}
</style>
"""
# Assemble marquee HTML
marquee_html = f"""
<div class="marquee-container">
    <span class="marquee-text">
        {marquee_text}
    </span>
</div>
"""

visualization_data = []
for category, entries in cryosphere_cracks.items():
    for entry in entries:
        # Skip entries with None values for latitude or longitude
        if entry["Longitude"] is not None:
            visualization_data.append(
                {
                    "name": entry["Region"],
                    "lat": entry["Latitude"],
                    "lng": entry["Longitude"],
                    "energy": entry["Elastic_Energy"] * 10,
                }
            )

# Convert to JSON format for embedding in JavaScript
visualization_data_json = json.dumps(visualization_data)

javascript_code = f"""
    import * as THREE from '//unpkg.com/three/build/three.module.js';

    const cryosphereCracksData = {visualization_data_json};

    const globe = Globe()
      (document.getElementById('globeViz'))
      .globeImageUrl('//unpkg.com/three-globe/example/img/earth-night.jpg')
      .backgroundColor('rgb(255, 255, 255)')
      .heatmapPointLat('lat')
      .heatmapPointLng('lng')
      .heatmapPointWeight('energy')
      .heatmapTopAltitude(0.1)
      .heatmapBandwidth(2.9)
      .heatmapColorSaturation(1.8)
      .enablePointerInteraction(true)
        .pointsData(cryosphereCracksData)
        .pointLat(d => d.lat)
        .pointLng(d => d.lng)
        .pointAltitude(d => -1.0) // Scale altitude to energy
        .pointColor(() => 'transparent')
        .pointRadius(4.5)
        .onPointHover(d => {{
            const tooltip = document.getElementById('tooltip');
        }});

    // Add cryosphere cracks data
    globe.heatmapsData([cryosphereCracksData]);

    // Add auto-rotation
    globe.controls().autoRotate = true;
    globe.controls().autoRotateSpeed = 2.6;
"""

html_code = f"""
<head>
<style> body {{ margin: 0em; }} </style>
<script src="//unpkg.com/globe.gl"></script>
<script src="//unpkg.com/three"></script>
<script src="//unpkg.com/solar-calculator"></script>
</head>

<body>
<div id="globeViz"></div>
<div id="tooltip" style="position: absolute; background: white; padding: 5px; border: 1px solid gray; display: none; pointer-events: none;"></div>
<div id="time"></div>

<script type="module">
    { javascript_code }
</script>
</body>
"""
col1, col2 = st.columns(2)
with col1:
    st.components.v1.html(html_code, height=700, width=700)

st.markdown(marquee_css + marquee_html, unsafe_allow_html=True)
