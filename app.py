import streamlit as st
from streamlit_labelstudio import st_labelstudio

config = """
      <View>
        <Image name="img" value="$image" brightnessControl="true" contrastControl="true" zoomControl="true" rotateControl="true"></Image>
        <RectangleLabels name="tag" toName="img">
          <Label value="Hello"></Label>
          <Label value="Moon"></Label>
        </RectangleLabels>
      </View>
    """

interfaces = [
  "panel",
  "update",
  "controls",
  # "side-column",
  # "completions:menu",
  # "completions:add-new",
  # "completions:delete",
  # "predictions:menu",
],

user = {
  'pk': 1,
  'firstName': "James",
  'lastName': "Dean"
},

task = {
  'completions': [],
  'predictions': [],
  'id': 1,
  'data': {
    'image': "https://htx-misc.s3.amazonaws.com/opensource/label-studio/examples/images/nick-owuor-astro-nic-visuals-wDifg5xc9Z4-unsplash.jpg"
  }
}

st.title('Labelstudio component')

# Store and display the return value of your custom component
results_raw = st_labelstudio(config, interfaces, user, task)


if results_raw is not None:
  areas = [v for k, v in results_raw['areas'].items()]

  results = []
  for a in areas:
    results.append({'id':a['id'], 'x':a['x'], 'y':a['y'], 'width':a['width'], 'height':a['height'], 'label':a['results'][0]['value']['rectanglelabels'][0]})

  st.table(results)
