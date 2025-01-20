import streamlit as st

if st.secrets["runtime"]["STATUS"] == "Production":
    st.set_page_config(
        page_title="Ice Ice Cracks",
        page_icon="✨",
        initial_sidebar_state="collapsed",
    )

    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        [data-testid="stHeader"] {
            display: none
            }
    </style>
    """,
        unsafe_allow_html=True,
    )


import json
from philoui.authentication_v2 import AuthenticateWithKey
from philoui.io import QuestionnaireDatabase as IODatabase
from philoui.io import (
    conn,
    create_dichotomy,
    create_equaliser,
    create_qualitative,
    create_quantitative,
)
from philoui.survey import CustomStreamlitSurvey

if "serialised_data" not in st.session_state:
    st.session_state.serialised_data = {}


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


mask_string = lambda s: f"{s[0:4]}***{s[-4:]}"


def authentifier(authenticator):
    (
        tab2,
        tab1,
    ) = st.tabs(["I am returning", "I am new"])

    with tab2:
        if st.session_state["authentication_status"] is None:
            authenticator.login("Connect", "main", fields=fields_connect)
            st.warning("Please use your access key")

        else:
            st.markdown(
                f"#### My access key is already forged, its signature is `{mask_string(st.session_state['username'])}`."
            )

    with tab1:
        if st.session_state["authentication_status"] is None:
            """
            There's a key in store.
            Click `Update keys database` after filling the captcha, to retrieve it. 
            """
            try:
                match = True
                success, access_key, response = authenticator.register_user(
                    data=match,
                    captcha=True,
                    pre_authorization=False,
                    fields=fields_forge2,
                )
                if success:
                    st.success("Key successfully forged")
                    st.toast(f"Access key: {access_key}")
                    st.session_state["username"] = access_key
                    st.markdown(
                        f"### Your access key is `{access_key}`. Now connect using the key and keep it safe! it will allow you to access the next steps."
                    )
            except Exception as e:
                st.error(e)
        else:
            st.info("It seems that I am already connected")
            # with col2:
            authenticator.logout()


# - **Purpose**: This initiative focuses on mapping knowledge about ice behavior, processes, and fracture phenomena, emphasizing scientific collaboration and interdisciplinary engagement.


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


def energy_globe_cracks(cryosphere_cracks):
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
      .globeImageUrl('//unpkg.com/three-globe/example/img/earth-water.png')
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


def marquee(cryosphere_cracks):
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

    st.markdown(marquee_css + marquee_html, unsafe_allow_html=True)


def nucleate(survey):
    name = survey.text_input("`Nice to meet you, what is your name?`")
    """
    ### Your input will help create a shared knowledge map, identifying gaps in understanding, and fostering meaningful exchange between researchers.
    """
    if name:
        st.success(f"Wonderful to have you onboard, {name}.")
        st.markdown("### One Thing to Know Before We Get Started:")
        st.markdown("""
    - **Privacy**: All shared data and responses are for collaborative research purposes only and will be handled confidentially.
    """)

        # Checkbox to acknowledge the terms
        agree = survey.checkbox("Acknowledged", key="acknowledge")

        if agree:
            st.success("Great! Let's move forward and connect.")
        else:
            st.warning("Do you acknowledge these guidelines?")


def _form_submit():
    with st.spinner("Checking your signature..."):
        signature = st.session_state["username"]
        serialised_data = st.session_state["serialised_data"]

        if not serialised_data:
            st.error(
                "No data available. Please ensure data is correctly entered before proceeding."
            )
        else:
            preferences_exists = db.check_existence(signature)
            st.write(f"Integrating preferences `{mask_string(signature)}`")
            _response = "Yes!" if preferences_exists else "Not yet"
            st.info(f"Some of your preferences exist...{_response}")

            try:
                data = {
                    "signature": signature,
                    "nucleation_01": json.dumps(serialised_data),
                }
                # throw an error if signature is null
                if not signature:
                    raise ValueError("Signature cannot be null or empty.")
                print(signature)

                existing_entry = (
                    conn.table("cryosphere")
                    .select("signature, nucleation_01")
                    .eq("signature", signature)
                    .execute()
                )
                if existing_entry:
                    existing_data = existing_entry.data[0]
                    # Deserialize the `nucleation_01` field if it exists
                    existing_nucleation = json.loads(
                        existing_data.get("nucleation_01", "{}")
                    )

                    # Deserialize the new `nucleation_01` field
                    new_nucleation = json.loads(data.get("nucleation_01", "{}"))

                    # Merge the new nucleation data into the existing one
                    merged_nucleation = {**existing_nucleation, **new_nucleation}

                    # Update the `nucleation_01` field with the merged data
                    existing_data["nucleation_01"] = json.dumps(merged_nucleation)
                else:
                    # No existing entry, use the new data as-is
                    existing_data = data

                query = (
                    conn.table("cryosphere")
                    .upsert(existing_data, on_conflict=["signature"])
                    .execute()
                )

                if query:
                    st.success("🎊 Preferences integrated successfully!")
                    st.balloons()

            except ValueError as ve:
                st.error(f"Data error: {ve}")
            except Exception as e:
                st.error("🫥 Sorry! Failed to update data.")
                st.write(e)


config = {
    "credentials": {"webapp": "cracks-players", "usernames": {}},
    "cookie": {
        "expiry_days": 20,
        "expiry_minutes": 30,
        "key": "ice_panel_cookie",
        "name": "ice_panel_cookie",
    },
    "preauthorized": {"emails": ""},
}

authenticator = AuthenticateWithKey(
    credentials=config["credentials"],
    cookie_name=config["cookie"]["name"],
    cookie_key=config["cookie"]["key"],
    cookie_expiry_days=config["cookie"]["expiry_days"],
    pre_authorized=config["preauthorized"],
)
fields_connect = {
    "Form name": "Open with your access key",
    "Email": "Email",
    "Username": "Username",
    "Password": "Password",
    "Repeat password": "Repeat password",
    "Register": " Retrieve access key ",
    "Captcha": "Captcha",
}
fields_forge = {
    "Form name": "I agree to share my vantage point",
    "Email": "Email",
    "Username": "Username",
    "Password": "Password",
    "Repeat password": "Repeat password",
    "Register": " Here • Now ",
    "Captcha": "Captcha",
}
fields_forge2 = {
    "Form name": "Register access key",
    "Email": "Email",
    "Username": "Username",
    "Password": "Password",
    "Repeat password": "Repeat password",
    "Register": " Update keys database ",
    "Captcha": "Captcha",
}

db = IODatabase(conn, "cryosphere")
survey = CustomStreamlitSurvey()

pages = survey.pages(6, on_submit=lambda: _form_submit())
if st.session_state["username"] is not None:
    f"""Signature : `{st.session_state["username"]}`"""

with pages:
    st.divider()
    # st.write(f"{pages.current} / {pages.n_pages}")
    st.progress(pages.current / pages.n_pages)
    if pages.current == 0:
        """
#### Mapping knowledge about ice behavior, processes, and fracture phenomena, emphasising scientific collaboration and interdisciplinary engagement requires your _agreement_.
"""
        if st.session_state["authentication_status"] is None:
            try:
                match = True
                col1, col, col3 = st.columns([0.1, 1, 0.1])
                with col:
                    success, access_key, response = authenticator.register_user(
                        data=match,
                        captcha=False,
                        pre_authorization=False,
                        fields=fields_forge,
                        key="Register new",
                    )
                    if success:
                        st.success(f"Key successfully forged.")
                        st.toast(f"Access key: {access_key}")
                        st.session_state["username"] = access_key
                        st.markdown(
                            f"### Your access key is `{access_key}`. Now connect using the key and keep it safe! it will allow you to access the next steps."
                        )

            except Exception as e:
                st.error(e)
        else:
            st.markdown(f"#### _Agreed._")

    if pages.current == 1:
        st.title("Why ice? What inspires you about studying ice? ")
        question = survey.text_input("My  point is...", id="question")
        hash_question = hash(question)
        """
        An open-ended question: a reflection on motivations, insights, and the significance of one's work in the larger context of glaciology."""

    if pages.current == 2:
        st.title("We are mapping an energy process.")
        st.markdown(
            """
            Cracks in ice systems show the interplay between energy accumulation, release, and dissipation. Understood but... 
            ## _When_ is the next big crack?
            
            Energy-based approaches may offer a lens to analyse these processes, quantifying stability transitions, from damage accumulation to crack nucleation and propagation. 

            ### Collaborative data exchange with glaciologists and other disciplines fosters insight-sharing, enabling models that integrate observations, theoretical advances, and numerical simulations.
                        
            """
        )
        # Highlighted regions approximately represent key sites of ice fracture activity, coarse mapping based on prior analysis environmental factors influencing ice dynamics.

    if pages.current == 3:
        """

            ## How to visualise, approximately, _where_ are new cracks nucleating?
        """

        energy_globe_cracks(cryosphere_cracks)
        """
            The plot provides an approximate estimate of energy concentration in ice, a zero-order global perspective on cryosphere vulnerability. _See the marquee for approximate locations of ice fracture activity._
        """
        marquee(cryosphere_cracks)

    if pages.current == 4:
        """
            # Expressing interest in a cryosph-fracture workshop?

        """
        # ask questio
        # question = survey.text_input("What would you like to learn about fractures in ice structures?", id="workshop")

        """
            ## Connecting for insights on fractures in ice structures

        """
        nucleate(survey)
    if pages.current == 5:
        """
#### Ice and cryospheric phenomena are complex and interconnected, their interest spanning across glaciology, mechanics, mathematics, and policy-making.
Mapping knowledge helps us to:
- Aggregate and organise scattered scientific knowledge.
- Identify underrepresented areas or gaps in research.
- Promote collaborative problem-solving approaches to critical challenges like ice sheet stability, sea-level rise, and cryosphere response to environmental change.    

"""

        """
        # _Submit your vantage point_ to shape an interactive and collaborative platform to map and bridge knowledge, foster interdisciplinary connection, and deepen our understanding of ice behaviour.

        """
st.divider()

st.session_state["serialised_data"] = survey.data

# st.json(st.session_state["serialised_data"])
# if st.button(
#     "Integrate the Bigger Picture",
#     key="integrate",
#     help="Integrate your data",
#     disabled=not bool(st.session_state["authentication_status"]),
#     type="primary",
#     use_container_width=True,
#     on_click=lambda: _form_submit(),
# ):
#     """
#     Congratulations!

# Save this page in your bookmarks and check again in a few days. Otherwise, reach out to me by email.

# leon.baldelli@cnrs.fr

# """


# By focusing on energetic thresholds and dissipation mechanisms, we refine our understanding of how fractures interact with environmental drivers like stress, strain, and fluid penetration.

# st.markdown("""
# We're excited to collaborate to explore and map the irreversible processes and behaviour of the cryosphere.
# Our aim is to create an interactive and collaborative platform to map knowledge and bridge its gaps, foster
# interdisciplinary connections, and deepen our understanding of ice behaviour.
# """)


st.divider()


authentifier(authenticator)
