# 080 Google Earth Engine in Python

Draft notes under development

## GEE

Google Earth Engine is a powerful cloud resource provided by Google that has found wide application in Earth Observation (EO) and related disciplines. 

The power of the tool comes from provision of the underlying processing tools on the remote cloud resource, **alongside** vast quantities of EO data. 

The purpose of this notebook is to provide a brief introduction to some of the basic GEE functionality, datasets and coding in Python.

### EE

The GEE library is imported as `ee`. When you want to use GEE resources, you will need to authenticate your account using a google login. We can set this going using `ee.Authenticate()`. This will pop up another browser window. 

You should follow the instructions on that to obtain an authentification code (e.g. `401AX4XfWj37NbOf5RnY4d4910lyW76yh2B0j9Rvj0aVqs9AVmf8oKM`) and initialise GEE (`ee.Initialize()`). You will only need to do that once per session.


```python
import ee

ee.Authenticate()
ee.Initialize()
```


<p>To authorize access needed by Earth Engine, open the following
        URL in a web browser and follow the instructions:</p>
        <p><a href=https://accounts.google.com/o/oauth2/auth?client_id=517222506229-vsmmajv00ul0bs7p89v5m89qs8eb9359.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fearthengine+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevstorage.full_control&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&code_challenge=2OI00sTloC_svLa7KJPAxJIcwORffBNnOdx4yzBDwvo&code_challenge_method=S256>https://accounts.google.com/o/oauth2/auth?client_id=517222506229-vsmmajv00ul0bs7p89v5m89qs8eb9359.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fearthengine+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevstorage.full_control&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&code_challenge=2OI00sTloC_svLa7KJPAxJIcwORffBNnOdx4yzBDwvo&code_challenge_method=S256</a></p>
        <p>The authorization workflow will generate a code, which you
        should paste in the box below</p>



    Enter verification code: 4/1AX4XfWiEu_p9CW1qMJ4Lv1pIZyYTeCK0IfwFy6N3ohAxZ5JLieVIxPFQT9Q\
    
    Successfully saved authorization token.


The main data types we need to be interested in for GEE are:

| Class | example | comment |  
|---:|---:|---:|
[Image](https://developers.google.com/earth-engine/guides/image_overview) | `image = ee.Image('JAXA/ALOS/AW3D30/V2_2')` | An image, often with multiple bands you can access with `image.bandNames()`
| [ImageCollection](https://developers.google.com/earth-engine/apidocs/ee-imagecollection) |`imageCollection = ee.ImageCollection("COPERNICUS/S2_SR")`| A collection (set) of `Image`s. You can e.g. use `imageCollection.map(lambda )`


For a full set of docs (in [Javascript, but very similar to Python](https://giswqs.medium.com/15-converting-earth-engine-javascripts-to-python-code-with-just-a-few-mouse-clicks-6aa02b1268e1)) in the [GEE API docs](https://developers.google.com/earth-engine/apidocs).

If we look at the example for `Image`, we can gain an insight into how GEE works:


```python
image = ee.Image('JAXA/ALOS/AW3D30/V2_2')
print(image.bandNames())
```

    ee.List({
      "functionInvocationValue": {
        "functionName": "Image.bandNames",
        "arguments": {
          "image": {
            "functionInvocationValue": {
              "functionName": "Image.load",
              "arguments": {
                "id": {
                  "constantValue": "JAXA/ALOS/AW3D30/V2_2"
                }
              }
            }
          }
        }
      }
    })


The reason this doesn't seem to be run, is there hat all of this code (and the rest resulting list) is server-side code. So all of this he internal prcessing, which is computationally efficient ads the processing happens on the same machines that hold the data (in effect). But we want to print the value of something, we want that information on the Client side, which is slow as it involves sending the data over the internet. You should [read more on the pghilisohpy](https://developers.google.com/earth-engine/guides/client_server) of clibnet-Server architechure and how to write cide in iyt



```python
imageCollection = ee.ImageCollection("COPERNICUS/S2_SR")a]
firstOne = imageCollection.map(lambda x : x.multiply(0.01))cd
```


```python
region = ee.Feature(ee.FeatureCollection('EPA/Ecoregions/2013/L3')\
  .filter(ee.Filter.eq('us_l3name', 'Sierra Nevada'))\
  .first());


idict = {
  'reducer': ee.Reducer.mean(),
  'geometry': region.geometry(),
  'scale': 30,
  'maxPixels': 1e9
}
print(idict)
# Reduce the region. The region parameter is the Feature geometry.
meanDictionary = image.reduceRegion(**idict)

# The result is a Dictionary.  Print it.
print(meanDictionary);
```

    {'reducer': <ee.Reducer object at 0x7fadcda97e90>, 'geometry': ee.Geometry({
      "functionInvocationValue": {
        "functionName": "Feature.geometry",
        "arguments": {
          "feature": {
            "functionInvocationValue": {
              "functionName": "Collection.first",
              "arguments": {
                "collection": {
                  "functionInvocationValue": {
                    "functionName": "Collection.filter",
                    "arguments": {
                      "collection": {
                        "functionInvocationValue": {
                          "functionName": "Collection.loadTable",
                          "arguments": {
                            "tableId": {
                              "constantValue": "EPA/Ecoregions/2013/L3"
                            }
                          }
                        }
                      },
                      "filter": {
                        "functionInvocationValue": {
                          "functionName": "Filter.equals",
                          "arguments": {
                            "leftField": {
                              "constantValue": "us_l3name"
                            },
                            "rightValue": {
                              "constantValue": "Sierra Nevada"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }), 'scale': 30, 'maxPixels': 1000000000.0}
    ee.Dictionary({
      "functionInvocationValue": {
        "functionName": "Image.reduceRegion",
        "arguments": {
          "geometry": {
            "functionInvocationValue": {
              "functionName": "Feature.geometry",
              "arguments": {
                "feature": {
                  "functionInvocationValue": {
                    "functionName": "Collection.first",
                    "arguments": {
                      "collection": {
                        "functionInvocationValue": {
                          "functionName": "Collection.filter",
                          "arguments": {
                            "collection": {
                              "functionInvocationValue": {
                                "functionName": "Collection.loadTable",
                                "arguments": {
                                  "tableId": {
                                    "constantValue": "EPA/Ecoregions/2013/L3"
                                  }
                                }
                              }
                            },
                            "filter": {
                              "functionInvocationValue": {
                                "functionName": "Filter.equals",
                                "arguments": {
                                  "leftField": {
                                    "constantValue": "us_l3name"
                                  },
                                  "rightValue": {
                                    "constantValue": "Sierra Nevada"
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "image": {
            "functionInvocationValue": {
              "functionName": "Image.load",
              "arguments": {
                "id": {
                  "constantValue": "JAXA/ALOS/AW3D30/V2_2"
                }
              }
            }
          },
          "maxPixels": {
            "constantValue": 1000000000.0
          },
          "reducer": {
            "functionInvocationValue": {
              "functionName": "Reducer.mean",
              "arguments": {}
            }
          },
          "scale": {
            "constantValue": 30
          }
        }
      }
    })


When we print this function, we might think that it would print out the band names for 'JAXA/ALOS/AW3D30/V2_2', but instead it returns data in an `ee.List` type that sets up a dictionary describing the hierachy of command we want to run.  

## GEEmap

One of the best resources built around the core GEE functionality is the `geemap` library from [https://github.com/giswqs](Qiusheng Wu) to provide a simple mapping front end. You will find a huge number of blog entries and tutorials with examples. 

`Wu, Q., (2020). geemap: A Python package for interactive mapping with Google Earth Engine. The Journal of Open Source Software, 5(51), 2305.` [https://doi.org/10.21105/joss.02305](https://doi.org/10.21105/joss.02305).

One thing to bear in mind with interactive processing in Jupyter notebooks in Python is that you need to be aware of which active window you are using. Notice that if yiou want to finish processing in one cell and run code in another cell, you need to stop the code running in the first cell (stop button on the control panel). 


## Image collections

First you might want to take a look at the datasets available on GEE by looking in the [dataset catalog](https://developers.google.com/earth-engine/datasets/catalog/). 

Suppose we want to develop a visualisation using Sentinel-2 MSI data. In that case, we could select the dataset `"COPERNICUS/S2_SR"`:



```python
s2 = ee.ImageCollection("COPERNICUS/S2_SR")

# what type?
type(s2)
```




    ee.imagecollection.ImageCollection



The variable `s2` contains an EE `ImageCollection`, which is the core data type for collections of raster spatial data assets. 

An image collection is made up of a group of images. The method `first()`, for example, selects the first image in the collection. 


```python
s2_image = s2.first()

# what type?
type(s2_image)
```




    ee.image.Image



To do some processing on this collection, the main functionality that processes or filters over the image collection are:

| Operation | example | comment |  
|---:|---:|---:|
| `filterBounds(geometry)` | `s2.filterBounds(ee.Geometry.Point(0.1276,51.5072))` | filter physical extent by defined geometry |  
| `filterDate(start, opt_end=None)` | `s2.filterDate('2019-01-01', '2019-12-31')`  | filter the collection by date |  
| `limit(n)` | `s2.limit(5)` | limit the number of images in the collection to `n` |  
| `map(algorithm)` | `s2.map()` | map `algorithm` to each image in the image collection  |  





| Operation | example | comment |  
|---:|---:|---:|
| `reduce(Reducer)` | `s2.reduce(ee.Reducer.median())` | Apply the reducer to the image collection. This results in a single |


```python
help(s2.map)
```

    Help on method map in module ee.collection:
    
    map(algorithm, opt_dropNulls=None) method of ee.imagecollection.ImageCollection instance
        Maps an algorithm over a collection.
        
        Args:
          algorithm: The operation to map over the images or features of the
              collection, a Python function that receives an image or features and
              returns one. The function is called only once and the result is
              captured as a description, so it cannot perform imperative operations
              or rely on external state.
          opt_dropNulls: If true, the mapped algorithm is allowed to return nulls,
              and the elements for which it returns nulls will be dropped.
        
        Returns:
          The mapped collection.
        
        Raises:
          ee_exception.EEException: if algorithm is not a function.
    



```python
# centre longitude,latitude
location = 0.1276, 51.5072
cloud_thresh = 30

collection = ee.ImageCollection("COPERNICUS/S2_SR")\
.filterBounds(ee.Geometry.Point(*location)).filterDate('2019-01-01', '2019-12-31') \
    .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', cloud_thresh))
```


```python
import ee
import geemap

# Create a map centered at (lon, lat).
Map = geemap.Map(center=location, zoom=10)

# Compute the median of each pixel for each band of the 5 least cloudy scenes.
median = collection.limit(5).reduce(ee.Reducer.median())

# Define visualization parameters in an object literal.
vizParams = {'bands': ['B4_median', 'B3_median', 'B2_median'],
             'min': 0, 'max': 3000, 'gamma': 1.3}

Map.setCenter(*location, 10)
Map.addLayer(median, vizParams, 'Median image')
# Display the map.
Map
```


    Map(center=[51.5072, 0.1276], controls=(WidgetControl(options=['position', 'transparent_bg'], widget=HBox(chil…



```python

```


```python
import ee
```


```python
help(geemap.ee_search)
```

    Help on function ee_search in module geemap.common:
    
    ee_search(asset_limit=100)
        Search Earth Engine API and user assets. If you received a warning (IOPub message rate exceeded) in Jupyter notebook, you can relaunch Jupyter notebook using the following command:
            jupyter notebook --NotebookApp.iopub_msg_rate_limit=10000
        
        Args:
            asset_limit (int, optional): The number of assets to display for each asset type, i.e., Image, ImageCollection, and FeatureCollection. Defaults to 100.
    



```python

```
