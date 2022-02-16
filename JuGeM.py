#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fontforge
import psMat
import os
import sys
from datetime import datetime

ASCENT = 1600
DESCENT = 400
FULLWIDTH = 2400
HALFWIDTH = 1200
SOURCE = os.getenv('JuGeM_SOURCE_FONTS_PATH', './sourceFonts')
LICENSE = open('./LICENSE.txt').read()
COPYRIGHT = open('./COPYRIGHT.txt').read()
VERSION = '0.0.2'
FAMILY = 'JuGeM'

fonts = [
    {
        "family": FAMILY,
        "name": FAMILY + "-Light",
        "filename": FAMILY + "-Light.ttf",
        "weight": 300,
        "weight_name": "Light",
        "style_name": "Light",
        "juliamono": "JuliaMono-Light.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Light.ttf",
        "juliamono_weight_reduce": -30,
        "jp_font_weight_add": 0,
        "italic": False,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-LightItalic",
        "filename": FAMILY + "-LightItalic.ttf",
        "weight": 300,
        "weight_name": "Light",
        "style_name": "Light Italic",
        "juliamono": "JuliaMono-LightItalic.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Light.ttf",
        "juliamono_weight_reduce": -30,
        "jp_font_weight_add": 0,
        "italic": True,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-Regular",
        "filename": FAMILY + "-Regular.ttf",
        "weight": 400,
        "weight_name": "Regular",
        "style_name": "Regular",
        "juliamono": "JuliaMono-Regular.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Regular.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": False,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-RegularItalic",
        "filename": FAMILY + "-RegularItalic.ttf",
        "weight": 400,
        "weight_name": "Regular",
        "style_name": "Italic",
        "juliamono": "JuliaMono-RegularItalic.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Regular.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": True,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-Bold",
        "filename": FAMILY + "-Bold.ttf",
        "weight": 700,
        "weight_name": "Bold",
        "style_name": "Bold",
        "juliamono": "JuliaMono-Bold.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Medium.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": False,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-BoldItalic",
        "filename": FAMILY + "-BoldItalic.ttf",
        "weight": 700,
        "weight_name": "Bold",
        "style_name": "Bold Italic",
        "juliamono": "JuliaMono-BoldItalic.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Medium.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": True,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-ExtraBold",
        "filename": FAMILY + "-ExtraBold.ttf",
        "weight": 800,
        "weight_name": "ExtraBold",
        "style_name": "ExtraBold",
        "juliamono": "JuliaMono-ExtraBold.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Bold.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": False,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-ExtraBoldItalic",
        "filename": FAMILY + "-ExtraBoldItalic.ttf",
        "weight": 800,
        "weight_name": "ExtraBold",
        "style_name": "ExtraBold Italic",
        "juliamono": "JuliaMono-ExtraBoldItalic.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Bold.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": True,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-Black",
        "filename": FAMILY + "-Black.ttf",
        "weight": 900,
        "weight_name": "Black",
        "style_name": "Black",
        "juliamono": "JuliaMono-Black.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Heavy.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": False,
    },
    {
        "family": FAMILY,
        "name": FAMILY + "-BlackItalic",
        "filename": FAMILY + "-BlackItalic.ttf",
        "weight": 900,
        "weight_name": "Black",
        "style_name": "Black Italic",
        "juliamono": "JuliaMono-BlackItalic.ttf",
        "jp_font": "GenJyuuGothicL-Monospace-Heavy.ttf",
        "juliamono_weight_reduce": 0,
        "jp_font_weight_add": 0,
        "italic": True,
    },
]

def log(_str):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + " " + _str)

def remove_glyph_from_juliamono(_font):
    """
    (現状使用しない)
    源柔ゴシックを採用したいグリフを JuliaMono から削除
    """
    glyphs = (
        list(range(0x3001, 0x3040))
        + list(range(0xFE10, 0xFE49))
        + list(range(0xFF01, 0xFF66))
        + list(range(0xFFE0, 0xFFE8))
    )

    for g in glyphs:
        _font.selection.select(g)
        _font.clear()

    return _font

def remove_glyph_from_jp_font(_font, jp_font_name):
    """
    JuliaMono を採用したいグリフを源柔ゴシックから削除
    """
    if jp_font_name == "GenJyuuGothicL-Monospace-Heavy.ttf":
        over_finish = 0x110618
    else:
        over_finish = 0x11061a
    glyphs = (
        list(range(0x0000, 0x2E7F + 0x1))
        # + list(range(0x3248, 0x325f + 0x1))
        + list(range(0x1D400, 0x1D7FF + 0x1))
        + list(range(0x1f100, 0x1f1a0 + 0x1))
        + list(range(0x110000, over_finish + 0x1))
    )

    for g in glyphs:
        _font.selection.select(g)
        _font.clear()

    return _font

def check_files():
    err = 0
    for f in fonts:
        if not os.path.isfile(os.path.join(SOURCE, f.get('juliamono'))):
            log('%s not exists.' % f)
            err = 1

        if not os.path.isfile(os.path.join(SOURCE, f.get('jp_font'))):
            log('%s not exists.' % f)
            err = 1

    if err > 0:
        sys.exit(err)

def align_to_center(_g):
    width = 0

    if _g.width > 1600:
        width = FULLWIDTH
    else:
        width = HALFWIDTH

    _g.width = width
    _g.left_side_bearing = _g.right_side_bearing = (_g.left_side_bearing + _g.right_side_bearing)/2
    _g.width = width

    return _g

def align_to_left(_g):
    width = _g.width
    _g.left_side_bearing = 0
    _g.width = width

def align_to_right(_g):
    width = _g.width
    bb = _g.boundingBox()
    left = width - (bb[2] - bb[0])
    _g.left_side_bearing = left
    _g.width = width

def fix_overflow(glyph):
    """
    上が 1600 を超えている、または下が -400 を超えているグリフを
    2000x2400 の枠にはまるように修正する
    ※全角のグリフのみに実施する
    """
    if glyph.width < FULLWIDTH:
        return glyph
    if glyph.isWorthOutputting:
        bb = glyph.boundingBox()
        height = bb[3] - bb[1]
        if height > 2000:
            # resize
            scale = 2000 / height
            glyph.transform(psMat.scale(scale, scale))
        bb = glyph.boundingBox()
        bottom = bb[1]
        top = bb[3]
        if bottom < -400:
            glyph.transform(psMat.translate(0, -400 - bottom))
        elif top > 1600:
            glyph.transform(psMat.translate(0, 1600 - top))
    return glyph

def add_lookup_gsub_single(font, lookup_name, single_list):
    """
    GSUB テーブルに Single Substitution lookup を追加する。
    """
    font.addLookup(lookup_name,'gsub_single', (), ())
    font.addLookupSubtable(lookup_name, f'{lookup_name}-1')
    for original, replace in single_list:
        glyph = font.createChar(-1, original)
        glyph.addPosSub(f'{lookup_name}-1', replace)

def add_my_style_set(font):
    """
    JuliaMono にパイプ記号(横向き三角)の
    文脈依存置換を有効化する 'ss21' feature を追加する。
    """
    single_list_1 = [
        ('bar', 'pipeleftfinish.alternate'),
        ('greater', 'pairright.alternate'),
        ('less', 'pipeleftstart.alternate')
    ]
    single_list_2 = [
        ('bar', 'piperightstart.alternate'),
        ('colon', 'doublecolonleft.alternate'),
        ('greater', 'piperightfinish.alternate')
    ]
    add_lookup_gsub_single(font, 'single1', single_list_1)
    add_lookup_gsub_single(font, 'single2', single_list_2)

    font.addLookup('ss21',
                    'gsub_contextchain',
                    (),
                    [['ss21', [['DFLT', ['dflt']], ['cyrl', ['BGR ', 'SRB ', 'dflt']], ['hebr', ['IWR ', 'dflt']], ['latn', ['AZE ', 'CAT ', 'CRT ', 'KAZ ', 'MOL ', 'NLD ', 'ROM ', 'TAT ', 'TRK ', 'dflt']]]]]
    )
    font.addContextualSubtable("ss21",
                                "ss21-1",
                                "glyph",
                                " | bar @<single2> greater @<single2> | "
    )
    font.addContextualSubtable("ss21",
                                "ss21-2",
                                "glyph",
                                " | less @<single1> bar @<single1> | "
    )

def build_font(_f, emoji):
    juliamono = fontforge.open(os.path.join(SOURCE, _f.get("juliamono")))
    add_my_style_set(juliamono)
    jp_font = fontforge.open(os.path.join(SOURCE, _f.get("jp_font")))
    log("remove_glyph_from_jp_font()")
    jp_font = remove_glyph_from_jp_font(jp_font, _f.get("jp_font"))

    log('transform juliamono')
    for g in juliamono.glyphs():
        if _f.get('juliamono_weight_reduce') != 0:
            g.changeWeight(_f.get('juliamono_weight_reduce'), 'auto', 0, 0, 'auto')
        g = align_to_center(g)

    if _f.get('jp_font_weight_add') != 0:
        for g in jp_font.glyphs():
            # g.changeWeight(_f.get('jp_font_weight_add'), 'auto', 0, 0, 'auto')
            g.stroke("caligraphic", _f.get('jp_font_weight_add'), _f.get('jp_font_weight_add'), 45, 'removeinternal')
            # g.stroke("circular", _f.get('jp_font_weight_add'), 'butt', 'round', 'removeinternal')

    ignoring_center = [
        0x3001,
        0x3002,
        0x3008,
        0x3009,
        0x300a,
        0x300b,
        0x300c,
        0x300d,
        0x300e,
        0x300f,
        0x3010,
        0x3011,
        0x3014,
        0x3015,
        0x3016,
        0x3017,
        0x3018,
        0x3019,
        0x301a,
        0x301b,
        0x301d,
        0x301e,
        0x3099,
        0x309a,
        0x309b,
        0x309c,
    ]
    log('transform jp_font')
    for g in jp_font.glyphs():
        g.transform(psMat.scale(1.82))
        full_half_threshold = 1600
        if _f.get('italic'):
            g.transform(psMat.skew(0.17))
            skew_amount = g.font.ascent * 1.82 * 0.17
            g.width = g.width + skew_amount
            full_half_threshold += skew_amount
        if g.width > full_half_threshold:
            width = FULLWIDTH
        else:
            width = HALFWIDTH
        g.transform(psMat.translate((width - g.width)/2, 0))
        g.width = width
        if g.encoding in ignoring_center:
            pass
        else:
            g = align_to_center(g)

    log('modify border glyphs')
    for g in jp_font.glyphs():
        if  g.isWorthOutputting:
            jp_font.selection.select(g.encoding)
            jp_font.copy()
            try:
                juliamono.selection.select(g.encoding)
                juliamono.paste()
            except Exception as ex:
                log("WARN: " + str(ex))

    log("fix_overflow()")
    for g in juliamono.glyphs():
        g = fix_overflow(g)
    juliamono.ascent = ASCENT
    juliamono.descent = DESCENT
    juliamono.upos = 45
    juliamono.fontname = _f.get('family')
    juliamono.familyname = _f.get('family')
    juliamono.fullname = _f.get('name')
    juliamono.weight = _f.get('weight_name')
    # juliamono = set_os2_values(juliamono, _f)
    juliamono.appendSFNTName(0x411,0, COPYRIGHT)
    juliamono.appendSFNTName(0x411,1, _f.get('family'))
    juliamono.appendSFNTName(0x411,2, _f.get('style_name'))
    # juliamono.appendSFNTName(0x411,3, "")
    juliamono.appendSFNTName(0x411,4, _f.get('name'))
    juliamono.appendSFNTName(0x411,5, "Version " + VERSION)
    juliamono.appendSFNTName(0x411,6, _f.get('family') + "-" + _f.get('weight_name'))
    # juliamono.appendSFNTName(0x411,7, "")
    # juliamono.appendSFNTName(0x411,8, "")
    # juliamono.appendSFNTName(0x411,9, "")
    # juliamono.appendSFNTName(0x411,10, "")
    # juliamono.appendSFNTName(0x411,11, "")
    # juliamono.appendSFNTName(0x411,12, "")
    juliamono.appendSFNTName(0x411,13, LICENSE)
    # juliamono.appendSFNTName(0x411,14, "")
    # juliamono.appendSFNTName(0x411,15, "")
    juliamono.appendSFNTName(0x411,16, _f.get('family'))
    juliamono.appendSFNTName(0x411,17, _f.get('style_name'))
    juliamono.appendSFNTName(0x409,0, COPYRIGHT)
    juliamono.appendSFNTName(0x409,1, _f.get('family'))
    juliamono.appendSFNTName(0x409,2, _f.get('style_name'))
    juliamono.appendSFNTName(0x409,3, VERSION + ";" + _f.get('family') + "-" + _f.get('style_name'))
    juliamono.appendSFNTName(0x409,4, _f.get('name'))
    juliamono.appendSFNTName(0x409,5, "Version " + VERSION)
    juliamono.appendSFNTName(0x409,6, _f.get('name'))
    # juliamono.appendSFNTName(0x409,7, "")
    # juliamono.appendSFNTName(0x409,8, "")
    # juliamono.appendSFNTName(0x409,9, "")
    # juliamono.appendSFNTName(0x409,10, "")
    # juliamono.appendSFNTName(0x409,11, "")
    # juliamono.appendSFNTName(0x409,12, "")
    juliamono.appendSFNTName(0x409,13, LICENSE)
    # juliamono.appendSFNTName(0x409,14, "")
    # juliamono.appendSFNTName(0x409,15, "")
    juliamono.appendSFNTName(0x409,16, _f.get('family'))
    juliamono.appendSFNTName(0x409,17, _f.get('style_name'))
    if emoji:
        fontpath = './dist/%s' % _f.get('filename')
    else:
        fontpath = './dist/noemoji/%s' % _f.get('filename')

    juliamono.generate(fontpath)

    jp_font.close()
    juliamono.close()

def main():
    check_files()
    for _f in fonts:
        log("Started: dist/noemoji/" + _f["filename"])
        build_font(_f, False)
        log("Finished: dist/noemoji/" + _f["filename"])
        log("")

if __name__ == '__main__':
    main()
