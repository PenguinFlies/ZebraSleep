# Data Walker

## Description
For Scanning Files, that's it.

## Requirement
Python >= 3.5
python-magic >= 0.4.12

## Usage
```python
import ReadData as rd
rd.data_walker(THE_MINI_DIRECTORY_PARSER, THE_FILE_GLOB_FILTER, MIME_TYPE, IGNORE_WHEN_DIRECTORY_IS_NOT_EXIST, VERBOSE)
```
The format of THE_MINI_DIRECTORY_PARSER:

```
[[The First Directories, False(No Need to be Parsed by Glob)], [The Second Directory Glob Format, True(Need to be Parsed by Glob)], ...]
```

## Example
If you want to collect the files which are under ```radar```
```
/home/data_collection
|-- 16-04-29
|   |-- FObs
|   |   |-- FML_OBS-2016-04-29T20:20:00+08:00.xml
|   |	| ...
|   |   `-- FML_OBS-2016-04-29T23:50:00+08:00.xml
|   |-- Obs
|   |   |-- OBS-2016-04-29T20:20:00+08:00.xml
|   |	| ...
|   |   `-- OBS-2016-04-29T23:40:00+08:00.xml
|   |-- Rain
|   |   |-- RAIN-2016-04-29T19:00:00+08:00.xml
|   |	| ...
|   |   `-- RAIN-2016-04-29T23:40:00+08:00.xml
|   |-- radar
|   |   |-- 2016-04-29T20:18:00+08:00.jpg
|   |	| ...
|   |   |-- 2016-04-29T23:30:00+08:00.jpg
|   |   `-- radar.xml
|   `-- thunder
|       |-- 16-04-29-20-31-46.kml
|   |	| ...
|-- 16-05-01
|   |-- ENH_SAT
|   |   |-- 2016-04-30T23:30:00+08:00.jpg
|   |	| ...
|   |   |-- 2016-05-01T23:30:00+08:00.jpg
|   |   `-- ENHSAT.xml
|   |-- FObs
|   |   |-- FML_OBS-2016-04-30T06:00:00+08:00.xml
|   |	| ...
|   |   `-- FML_OBS-2016-05-01T23:50:00+08:00.xml
|   |-- Obs
|   |   |-- OBS-2016-04-30T23:40:00+08:00.xml
|   |	| ...
|   |   `-- OBS-2016-05-01T23:40:00+08:00.xml
|   |-- Rain
|   |   |-- RAIN-2016-04-30T23:50:00+08:00.xml
|   |	| ...
|   |   `-- RAIN-2016-05-01T23:40:00+08:00.xml
|   |-- radar
|   |   |-- 2016-05-01T00:12:00+08:00.jpg
|   |	| ...
|   |   |-- 2016-05-01T23:36:00+08:00.jpg (But the actual file is a plain/text)
|   |   `-- radar.xml
|   `-- thunder
|   |   |-- 16-05-01-00-00-06.kml
|   |	| ...
|   |   `-- 16-05-01-23-54-02.kml
| ...

```

Use Data Walker

```python
import ReadData as rd
rd.data_walker([['/home/data_collection', False], ['*-*-*', True], ['radar', False]], '*.jpg', True, False)
```

Output

```
[['/home/data_collection/16-04-29/radar', '2016-04-29T20:18:00+08:00.jpg'],
...
['/home/data_collection/16-04-29/radar', '2016-04-29T23:30:00+08:00.jpg'],
['/home/data_collection/16-05-01/radar', '2016-05-01T00:12:00+08:00.jpg'],
...
['/home/data_collection/16-05-01/radar', '2016-05-01T23:36:00+08:00.jpg']]
```

If you want to verify the real mime_type is equal to its extensions, using the ```MIME_TYPE```;
the function would check the real mime type with unix ```file``` command and avoid the fake extensions name from adding to the return list.

For example

```python
rd.data_walker([['/home', False]], '*.jpg', "image/jpeg", True, False)
```

Output

```
[['/home/data_collection/16-04-29/radar', '2016-04-29T20:18:00+08:00.jpg'],
...
['/home/data_collection/16-04-29/radar', '2016-04-29T23:30:00+08:00.jpg'],
['/home/data_collection/16-05-01/radar', '2016-05-01T00:12:00+08:00.jpg'],
...]
```

The output will exclude the file extension "*.jpg" but the content isn't a valid image jpeg file.
