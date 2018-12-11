# Decal4Ortho
Add texture decals to Ortho4XP x-plane ortho sceneries

## Requirements

First install the required python modules with pip. At the moment the current required modules are:

 + docopt

You can install them with this command

```
pip install -r requirements.txt
```

## Usage


```
Usage:
  Decal4Ortho.py [--decal DECAL] [--remove DECAL | --remove-all | --replace DECAL] [--ex-com COMMAND]... [options] (DIRECTORY...)
  Decal4Ortho.py (-h | --help)
  Decal4Ortho.py --version

Options:
  -h --help            Show this screen.
  --version            Show version.
  --decal DECAL        Decal to apply. Suggested decals to try are:
                       DEFAULT (lib/g10/decals/maquify_1_green_key.dcl)
                       lib/g10/decals/grass_and_asphalt_green_key.dcl
  --remove DECAL       Remove the specified decal
  --remove-all         Remove all decals
  --replace DECAL      Replace this decal with the specified decal.
  --ex-com COMMAND     Exclude files with these commands [default: WET]
                       Set to NONE if you don't wish to exclude any files.
  --extension EXT      File extension to apply changes to [default: ter]   
  --debug              Print debug info   
```

## Example

Let's say you've got a bunch of ortho photo sceneries in your `Custom Scenery` directory:

```
 zOrtho4XP_-34+151
 zOrtho4XP_-35+151
 zOrtho4XP_-44+172
 zOrtho4XP_-44+173
 zOrtho4XP_-45+168
```

**WARNING**: This tool will modify your scenery files, please back up before before running. I will probably create a preview mode soon which allows you to preview what will be changed before applying the change.

Now to add the default `lib/g10/decals/maquify_1_green_key.dcl` decal to these sceneries quickly and easily you can execute the following command:

```
python Decal4Ortho.py --decal DEFAULT "path/to/Custom Scenery/zOrtho4XP_"*
```

Using this command with the wildcard `*` at the end will match to all `zOrtho4XP_` directories.

If you want to remove all decals after adding them, you can do the same with the following command:

```
python Decal4Ortho.py --remove-all "path/to/Custom Scenery/zOrtho4XP_"*
```
