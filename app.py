import streamlit as st
from streamlit_labelstudio import st_labelstudio


config = """
      <View>
        <Image name="img" value="$image"></Image>
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
  "side-column",
  "completions:menu",
  "completions:add-new",
  "completions:delete",
  "predictions:menu",
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

# Store and display the return value of your custom component
v = st_labelstudio(config, interfaces, user, task)
st.write(v)