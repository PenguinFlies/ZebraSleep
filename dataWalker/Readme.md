# Data Walker

## Description
For Scanning Files, that's it.

## Usage
```python
import ReadData as rd
rd.data_walker(THE_MINI_DIRECTORY_PARSER, THE_FILE_REGEX_FILTER, IGNORE_WHEN_DIRECTORY_IS_NOT_EXIST, VERBOSE)
```
The format of THE_MINI_DIRECTORY_PARSER:

```
[[The First Directories, False(No Need to be Parsed by Regex)], [The Second Directory Regex Format, True(Need to be Parsed by Regex)], ...]
```

## Example
If you want to collect the files which are under ```radar```
```
|-------root
	|-------/home
		|-------/data_collection
			|-------/16-06-01
			...	|-------/radar
			...		|-------/2016-06-01T0000.jpg
			...		...
			...		|-------/2016-06-01T2356.jpg
			|-------/16-06-31
				|-------/radar
					|-------/2016-06-31T0000.jpg
					...
					|-------/2016-06-31T2356.jpg
```

Use Data Walker

```python
import ReadData as rd
rd.data_walker([['/home/data_collection', False], ['*-*-*', True], ['radar', False]], '*.jpg', True, False)
```

Output

```
[['/home/data_collection/16-06-01/radar', 2016-06-01T0000.jpg], ... ['/home/data_collection/16-06-31/radar', 2016-06-31T2356.jpg]]
```
