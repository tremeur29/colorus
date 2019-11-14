# `colorus`

Sets powerlevel9k prompt to use up to 5 colours from colour schemes generated by `pywal`.

## Acknowledgements

Uses python3-<span title="i.e. just changing print x to print(x), it wasn’t that strenuous">compatible</span> version of [this gist](https://gist.github.com/naupaka/a300868203f32906717a1644c1c6f0d7)

## How to use

Add the line `. ~/.colourvars` to `.zshrc`, probably before powerlevel9k settings.

Use the following variables in those settings instead of specifying terminal colours: `$LINE1`, `$LINE2`, … `$LINE5`

e.g.

```
POWERLEVEL9K_CUSTOM_PROMPT_FOREGROUND="$LINE1"
```

Add this function to `.zshrc`, replacing `PATHTOCOLORUS` as appropriate:

```
pywal() {
        wal -i "$1" # plus any other options usually invoked with wal
        PATHTOCOLORUS/convert.sh
}
```

Then call `pywal` instead of `wal` (or any other name you choose to give the new function), specifying the source image as usual. Prompt colours will refresh when you open a new terminal.

## Potential issues/improvements

* Not sure how well this would work with dark terminal themes/without clear p9k backgrounds (only tested my own slightly controversial preferred settings).
* Specific colours can’t be assigned to particular uses.
* Would be good to use more than 5 colours if that many are generated.

## Details

First part of `convert.sh` (up to line 16) calls `colours.py` (the [downloaded script](https://gist.github.com/naupaka/a300868203f32906717a1644c1c6f0d7) that converts hex colour codes to Xterm ones) for each colour listed in the `wal` output file, `~/.cache/wal/colors`, and outputs the result to a file.

`convert.sh` then calls `strip.py`, which strips each line of this file to the actual Xterm colour code.

`convert.sh` removes duplicate lines from this file, and then calls `pad.py`, which assigns the list of colours to shell variables to be called in `.zshrc`.
