# 201 Google Earth Engine

## Introduction


### Purpose

In this notebook, we introduce the python interface to [Google Earth Engine](https://earthengine.google.com) (GEE) using the [`geemap`](https://github.com/giswqs/geemap) package.

We use GEE to explore some Earth Observation datasets and their characteristics and learn about interpreting quality control data.


We do not intend this to be a complete course on using GEE, and we do not want you spending all of your time developing in GEE at the moment: this is a course in scientific programming using Python and so needs to be more general. This then, it is a one-session introduction to some important datasets, the core ideas of processing in GEE, and some of the core methods you might use. When you want to develop your own codes, you will find the [`geemap` documentation](https://github.com/giswqs/geemap) and [examples](https://github.com/giswqs/earthengine-py-notebooks) of great use. 




### Prerequisites

You will need some understanding Python basics from part 1 of this course (notebooks with the code [`1??`](.))

You will also need to make sure you have a [google account](https://support.google.com/accounts/answer/27441?hl=en) to be able to use GEE, and will need to know your username and password. In addition, you will need to sign up for a GEE account. You need to request this by filling out the form at [signup.earthengine.google.com]( https://signup.earthengine.google.com/). **You will need to do this before we start the class** as you will need to wait for approval from Google.

### Timing

The session should take around 30 minutes to initially explore, though you could spend a lifetime looking at all of the datasets!

## Earth Engine

### What is GEE?

Google Earth Engine (GEE) is a facility for access to vast quantities of Earth Observation (EO) data, as well as many other geospatial datasets. It is a hugely valuable resource for scientists, as well as making a significant contribution to the democratisation of EO: anyone can sign up for a google account and use these resources to both access and process data. With a little coding experience, anyone can develop their own products or analyses.

You will find an increasingly large range of projects and [examples](https://earthengine.google.com/case_studies/) available. For more information on GEE, see the [GEE FAQ](https://earthengine.google.com/faq/). You can develop and deploy your own apps either using GEE on google Cloud [example](https://plewis.users.earthengine.app/view/nceo-united-kingdom), or hosted on other resources such as [heroku](https://github.com/giswqs/earthengine-apps) ([example](https://geemap-demo.herokuapp.com)).

There are some complexities and limitations to GEE that you should understand as well. In particular, whilst you can do some truly amazing things using GEE resources, they are provided free to you, and so there are limits to the amount of processing you can do at any one time, as well as quite strict limits on the amount of GEE local storage made available to you. You can certainly do great science within GEE, but to be a good coder, you will need wider exposure to accessing datasets than just through GEE.

### Interfaces

#### Code editor

The main interface to GEE is through the [web-based code editor](https://code.earthengine.google.com/). There is a good set of [documentation on this](https://developers.google.com/earth-engine/guides/getstarted) that you can browse through at a later date. In the code editor, you can run and develop [JavaScript](https://www.javascript.com/) codes, access saved datasets and documentation, and gain some basic experience of using GEE. Although we have not taught you JavaScript, you will notice that it is a high-level language with many similarities to Python. The GEE [guide for Python installation](https://developers.google.com/earth-engine/guides/python_install) provides some succinct advice and examples of common syntax differences between JavaScript and Python. In addition, there are resources available to allow you to [translate GEE JavaScript codes into Python](https://github.com/giswqs/geemap/blob/master/examples/notebooks/15_convert_js_to_py.md).

As a follow-up to this class, we suggest that you look in the `Scripts` tab of the [code editor](https://code.earthengine.google.com/), and try out one or more of the examples under the `Examples` list, for example, `Examples -> ImageCollection -> Landsat Simple Composite`. To use this, you need do no more than load the code by clicking on it, then click on the `Run` button. This example is a good one to start with: if you pan out in the viewer window you will see that GEE can process this 30 m resolution dataset *anywhere in the world* for you, in near real-time. It is showing a composite of all of the Landsat images over 6 months in 2015, between the dates `2015-1-1` and `2015-7-1`. To do this requires only around 4 lines of code. This is an amazing feat.

#### QGIS

Users of the popular [`QGIS`](https://qgis.org/en/site/) tool will be interested to know that GEE is available as a plugin. One version of this using the Python package [`ee`](https://anaconda.org/conda-forge/earthengine-api) is [plugin to QGIS](https://gee-community.github.io/qgis-earthengine-plugin/).

#### ee and geemap

We will also be using the [`ee`](https://anaconda.org/conda-forge/earthengine-api) Python package to access GEE, but with the [`geemap`](https://github.com/giswqs/geemap) package providing the mapping front-end.  [`geemap`](https://github.com/giswqs/geemap) has very good documentation and an excellent range of [examples](https://github.com/giswqs/earthengine-py-notebooks). This should make it much easier for you to access GEE.




### GEE datasets

A fundamental part of GEE is the vast quantities of data that it gives access to. The core datasets are described in the [GEE data catalog](https://developers.google.com/earth-engine/datasets). The GEE code that you write has straightforward access to any or all of these datasets and, importantly, is able to process them using GEE resources. 

You do not need to download the datasets, and do not need to know great details of what goes on internally in the engine to use GEE. But, as we will see, you still need to think carefully about any interpretation of the data.

You should spend some time after the class exploring the GEE datasets in the [data catalog](https://developers.google.com/earth-engine/datasets), but for this session, we will concentrate on the following quantities:

* Surface Reflectance
* Leaf Area Index


#### Leaf Area Index

The data product [MOD15](https://modis.gsfc.nasa.gov/data/dataprod/mod15.php) LAI/FPAR has been generated from NASA MODIS sensors Terra and Aqua data since 2002. We are now in dataset collection 6 (the data version to use).

    LAI is defined as the one-sided green leaf area per unit ground area in broadleaf canopies and as half the total needle surface area per unit ground area in coniferous canopies. FPAR is the fraction of photosynthetically active radiation (400-700 nm) absorbed by green vegetation. Both variables are used for calculating surface photosynthesis, evapotranspiration, and net primary production, which in turn are used to calculate terrestrial energy, carbon, water cycle processes, and biogeochemistry of vegetation. Algorithm refinements have improved quality of retrievals and consistency with field measurements over all biomes, with a focus on woody vegetation.

https://developers.google.com/earth-engine/datasets/tags/lai

https://developers.google.com/earth-engine/datasets/tags/crop


```python
import ee
import geemap
```


```python
Map = geemap.Map()
Map

```


    Map(center=[40, -100], controls=(WidgetControl(options=['position'], widget=HBox(children=(ToggleButton(value=…



```python
point = ee.Geometry.Point([-87.7719, 41.8799])

image = ee.ImageCollection('MODIS/006/MCD15A3H') \
    .filterBounds(point) \
    .filterDate('2019-01-01', '2019-12-31') \
    .max() \
    .select('Lai')

vis_params = {
    'min': 0,
    'max': 60,
    'bands': ['Lai']
}

Map.centerObject(point, 8)
Map.addLayer(image, vis_params, "MODIS LAI")
```


```python
props = geemap.image_props(image)
props.getInfo()
```


    ---------------------------------------------------------------------------

    HttpError                                 Traceback (most recent call last)

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in _execute_cloud_call(call, num_retries)
        344   try:
    --> 345     return call.execute(num_retries=num_retries)
        346   except googleapiclient.errors.HttpError as e:


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/googleapiclient/_helpers.py in positional_wrapper(*args, **kwargs)
        133                     logger.warning(message)
    --> 134             return wrapped(*args, **kwargs)
        135 


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/googleapiclient/http.py in execute(self, http, num_retries)
        906         if resp.status >= 300:
    --> 907             raise HttpError(resp, content, uri=self.uri)
        908         return self.postproc(resp, content)


    HttpError: <HttpError 400 when requesting https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/value:compute?prettyPrint=false&alt=json returned "Date: Parameter 'value' is required.">

    
    During handling of the above exception, another exception occurred:


    EEException                               Traceback (most recent call last)

    <ipython-input-4-02ced7a4e17a> in <module>
          1 props = geemap.image_props(image)
    ----> 2 props.getInfo()
    

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/computedobject.py in getInfo(self)
         93       The object can evaluate to anything.
         94     """
    ---> 95     return data.computeValue(self)
         96 
         97   def encode(self, encoder):


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in computeValue(obj)
        708             body={'expression': serializer.encode(obj, for_cloud_api=True)},
        709             project=_get_projects_path(),
    --> 710             prettyPrint=False))['result']
        711   return send_('/value', {
        712       'json': obj.serialize(for_cloud_api=False),


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in _execute_cloud_call(call, num_retries)
        345     return call.execute(num_retries=num_retries)
        346   except googleapiclient.errors.HttpError as e:
    --> 347     raise _translate_cloud_exception(e)
        348 
        349 


    EEException: Date: Parameter 'value' is required.



```python
props.get('IMAGE_DATE').getInfo()

```


    ---------------------------------------------------------------------------

    HttpError                                 Traceback (most recent call last)

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in _execute_cloud_call(call, num_retries)
        344   try:
    --> 345     return call.execute(num_retries=num_retries)
        346   except googleapiclient.errors.HttpError as e:


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/googleapiclient/_helpers.py in positional_wrapper(*args, **kwargs)
        133                     logger.warning(message)
    --> 134             return wrapped(*args, **kwargs)
        135 


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/googleapiclient/http.py in execute(self, http, num_retries)
        906         if resp.status >= 300:
    --> 907             raise HttpError(resp, content, uri=self.uri)
        908         return self.postproc(resp, content)


    HttpError: <HttpError 400 when requesting https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/value:compute?prettyPrint=false&alt=json returned "Date: Parameter 'value' is required.">

    
    During handling of the above exception, another exception occurred:


    EEException                               Traceback (most recent call last)

    <ipython-input-5-3c50e153c167> in <module>
    ----> 1 props.get('IMAGE_DATE').getInfo()
    

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/computedobject.py in getInfo(self)
         93       The object can evaluate to anything.
         94     """
    ---> 95     return data.computeValue(self)
         96 
         97   def encode(self, encoder):


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in computeValue(obj)
        708             body={'expression': serializer.encode(obj, for_cloud_api=True)},
        709             project=_get_projects_path(),
    --> 710             prettyPrint=False))['result']
        711   return send_('/value', {
        712       'json': obj.serialize(for_cloud_api=False),


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in _execute_cloud_call(call, num_retries)
        345     return call.execute(num_retries=num_retries)
        346   except googleapiclient.errors.HttpError as e:
    --> 347     raise _translate_cloud_exception(e)
        348 
        349 


    EEException: Date: Parameter 'value' is required.



```python
props.get('CLOUD_COVER').getInfo()

```


    ---------------------------------------------------------------------------

    HttpError                                 Traceback (most recent call last)

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in _execute_cloud_call(call, num_retries)
        344   try:
    --> 345     return call.execute(num_retries=num_retries)
        346   except googleapiclient.errors.HttpError as e:


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/googleapiclient/_helpers.py in positional_wrapper(*args, **kwargs)
        133                     logger.warning(message)
    --> 134             return wrapped(*args, **kwargs)
        135 


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/googleapiclient/http.py in execute(self, http, num_retries)
        906         if resp.status >= 300:
    --> 907             raise HttpError(resp, content, uri=self.uri)
        908         return self.postproc(resp, content)


    HttpError: <HttpError 400 when requesting https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/value:compute?prettyPrint=false&alt=json returned "Date: Parameter 'value' is required.">

    
    During handling of the above exception, another exception occurred:


    EEException                               Traceback (most recent call last)

    <ipython-input-6-b347f70f7d81> in <module>
    ----> 1 props.get('CLOUD_COVER').getInfo()
    

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/computedobject.py in getInfo(self)
         93       The object can evaluate to anything.
         94     """
    ---> 95     return data.computeValue(self)
         96 
         97   def encode(self, encoder):


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in computeValue(obj)
        708             body={'expression': serializer.encode(obj, for_cloud_api=True)},
        709             project=_get_projects_path(),
    --> 710             prettyPrint=False))['result']
        711   return send_('/value', {
        712       'json': obj.serialize(for_cloud_api=False),


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/ee/data.py in _execute_cloud_call(call, num_retries)
        345     return call.execute(num_retries=num_retries)
        346   except googleapiclient.errors.HttpError as e:
    --> 347     raise _translate_cloud_exception(e)
        348 
        349 


    EEException: Date: Parameter 'value' is required.



```python

```
