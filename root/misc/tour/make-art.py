#!/usr/bin/env python3

import os
import sys
import json

class Character:
    def __init__(self, c):
        self.char = c
        self.box_class = ""
        self.href = ""

def print_css(box_info):
    print("<style>.tour_msg{display:none;background:#000;border:1px solid #0f0;max-width:300px;padding:3px;}#tour_art{font-family:monospace;position:relative;}",end="")
    for obj in box_info:
        obj_class = obj["class"]
        print(".tour_span_%s:hover~#tour_msg_%s{display:block;}" % (obj_class, obj_class), end="")
    print("</style>",end="")

def print_js():
    # https://stackoverflow.com/questions/49301668/
    code = """<script>
let $msgs = document.getElementsByClassName("tour_msg");
let $art = document.getElementById("tour_art");
for (var $i = 0; i < msgs.length; ++i) {
    msgs[i].style["position"] = "absolute";
}
let $mx = 0;
let $my = 0;
window.addEventListener("mousemove", function(e) {
    mx = e.clientX;
    my = e.clientY;
});
function $step(timestamp) {
    var $square = art.getBoundingClientRect();
    for (var $i = 0; i < msgs.length; ++i) {
        var $elem = msgs[i];
        elem.style.top  = (my - square.y + 15) + "px";
        elem.style.left = (mx - square.x + 15) + "px";
    }
    window.requestAnimationFrame(step);
}
window.requestAnimationFrame(step);
</script>"""
    # goofy js minifier
    new_code = ""
    for char in code:
        if char == ' ' or char == '\n':
            continue
        if char == '$':
            char = ' '
        new_code += char
    print(new_code,end="")

def make_rich_art(text_file, box_info):
    rich_text = []
    for line in text_file:
        rich_line = []
        for char in line:
            rich_line.append(Character(char))
        rich_text.append(rich_line)
    for box in box_info:
        for location in box["location"]:
            box_class = box["class"]
            href = ""
            if "href" in box:
                href = box["href"]
            start_row = location[0]-1
            start_col = location[1]-1
            end_row = location[2]
            end_col = location[3]
            for row in range(start_row, end_row):
                for col in range(start_col, end_col):
                    rich_text[row][col].box_class = box_class
                    rich_text[row][col].href = href
    return rich_text

def maybe_print_span_end(curr_span, rich_char):
    if curr_span.box_class == rich_char.box_class:
        return
    if curr_span.box_class == "":
        return
    if curr_span.href != "":
        print("</a>",end="")
    print("</span>",end="")

def maybe_print_span_start(curr_span, rich_char):
    if curr_span.box_class == rich_char.box_class:
        return
    if rich_char.box_class == "":
        return
    print("<span class=tour_span_%s>" % (rich_char.box_class),end="")
    if rich_char.href != "":
        print("<a class=hiddenlink href=%s>" % (rich_char.href),end="")

def html_escape_char(char):
    if char == '&': return "&amp;"
    if char == '<': return "&lt;"
    if char == '>': return "&gt;"
    if char == ' ': return "&nbsp;"
    return char

def print_rich_art(rich_art):
    curr_span = Character("")
    for row_index in range(len(rich_art)):
        row = rich_art[row_index]
        for col_index in range(len(row)):
            rich_char = row[col_index]
            maybe_print_span_end(curr_span, rich_char)
            if col_index == 0 and row_index != 0:
                print("<br>",end="")
            maybe_print_span_start(curr_span, rich_char)
            print(html_escape_char(rich_char.char),end="")
            curr_span = rich_char
    print("<br><br>",end="")

def print_info_boxes(box_info):
    for box in box_info:
        print("<div id=tour_msg_%s class=tour_msg>%s</div>" % (box["class"], box["text"]),end="")

def main():
    if len(sys.argv) < 3:
        print("Usage: %s [picture.txt] [box file.json]" % (sys.argv[0]))
        return
    text_file_path = sys.argv[1]
    box_file_path = sys.argv[2]
    with open(text_file_path, "r") as f:
        text_file = [line[:-1] for line in f.read().split("\n")[:-1]]
    with open(box_file_path, "r") as f:
        box_info = json.loads(f.read())

    print("```{=html}")
    print_css(box_info)
    rich_art = make_rich_art(text_file, box_info)
    print("<div id=tour_art>",end="")
    print_rich_art(rich_art)
    print_info_boxes(box_info)
    print("</div>",end="")
    print_js()
    print("\n```")

if __name__ == '__main__':
    olddir = os.getcwd()
    os.chdir(os.path.dirname(sys.argv[0]))
    main()
    os.chdir(olddir)
