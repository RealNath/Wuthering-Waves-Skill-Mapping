# Wuthering Waves Skill Mapping
A simple program (Python project) I made out of boredom to automatically format character's skill (kits) from a certain anime game using Dimbreath's WutheringData.

## How to Use
* Download [Skill.json](https://github.com/Dimbreath/WutheringData/blob/master/ConfigDB/Skill.json) and [MultiText.json](https://github.com/Dimbreath/WutheringData/blob/master/TextMap/en/MultiText.json) from Wuthering Data.
* Put it in the same directory/folder as the Python code.
* Run either the executable (.exe) or Python file.
  * **.exe** - run instantly (double click it)
  * **Python** - Download Python (obviously), Pandas (`pip install pandas`), NumPy (`pip install numpy`); open command line, execute: `python skillmapping.py`
* Type in the skill's/kit's ID or name (e.g `1000101` or `feather as blade`)
  * capitalization doesn't matter (case insensitive)

## But why did you make this?
I was adding [Xiangli Yao's kit descriptions](https://wutheringwaves.fandom.com/wiki/Xiangli_Yao/Combat) to the wiki (my username is [Real_Nath](https://wutheringwaves.fandom.com/wiki/User:Real_Nath) btw), turns out many skill descriptions have numbers seperated from text, and I need to convert it to the wiki format too. Here's an example from another character:
### Zhezhi's Resonance Skill - Manifestation
```
Summon <color=Highlight>Inklit Spirits</color> for assistance.\nCan be cast in mid-air.\n<size=10></size>\n<size=40><color=Title>Inklit Spirit</color></size>\nWhen the active Resonator deals DMG, an <color=Highlight>Inklit Spirit</color> will be summoned to perform a Coordinated Attack, dealing <color=Ice>Glacio DMG</color>, considered as Basic Attack DMG.\n-For {0} seconds after dealing DMG, 1 <color=Highlight>Inklit Spirit</color> is summoned per second. This effect can trigger once per second. Damage dealt by an Inklit Spirit does not trigger this effect.\n-Up to {1} <color=Highlight>Inklit Spirit</color> can be summoned every second, and up to {2} in total.\n-This effect lasts for {3}s, or until max <color=Highlight>Inklit Spirits</color> are summoned.
```
I want to find where the numbers `{0}`, `{1}`, etc are linked to. And I want to convert `<color=Highlight>Inklit Spirits</color>`, etc to the wiki format. Doing it manually for many descriptions is tiring, so I made a Python code to hone my programming skills too.

## Why do I need to download the 2 JSON files manually?
My plan was to fetch the data/text from each file's raw.githubusercontent.com at first, but there are thousands of lines, even MultiText.json has 75,278 data (key-value pairs). It takes forever (probably crash? not even Ctrl+C works), whether using the urllib or requests library.

## Credits
[Wuthering Data](https://github.com/Dimbreath/WutheringData) by Dimbreath
