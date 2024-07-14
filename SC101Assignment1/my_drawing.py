"""
Title: TSMC components
Name: YI HSIU
----------------------
Idea: TSMC symbols and some critical components of the circuits
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow

window = GWindow(1000, 800)

die_size = 80


def main():
    """
    TODO:
    """
    # to maker wafer
    wafer = GOval(500, 490)
    wafer.color = 'grey'
    wafer.filled = True
    wafer.fill_color = 'lightcyan'
    window.add(wafer, 500, 300)
    die1 = GRect(die_size, die_size)
    die1.filled = True
    die1.fill_color = 'lightgrey'
    window.add(die1, wafer.x+(window.width-wafer.x)*0.5+5, wafer.y+20)
    die2 = GRect(die_size, die_size)
    die2.filled = True
    die2.fill_color = 'lightgrey'
    window.add(die2, wafer.x+(window.width-wafer.x)*0.5+5, wafer.y+110)
    die3 = GRect(die_size, die_size)
    die3.filled = True
    die3.fill_color = 'lightgrey'
    window.add(die3, wafer.x+(window.width-wafer.x)*0.5+5, wafer.y+200)
    die4 = GRect(die_size, die_size)
    die4.filled = True
    die4.fill_color = 'lightgrey'
    window.add(die4, wafer.x+(window.width-wafer.x)*0.5+5, wafer.y+290)
    die5 = GRect(die_size, die_size)
    die5.filled = True
    die5.fill_color = 'lightgrey'
    window.add(die5, wafer.x+(window.width-wafer.x)*0.5+5, wafer.y+380)
    die6 = GRect(die_size, die_size)
    die6.filled = True
    die6.fill_color = 'lightgrey'
    window.add(die6, wafer.x+(window.width-wafer.x)*0.5+90, wafer.y+110)
    die7 = GRect(die_size, die_size)
    die7.filled = True
    die7.fill_color = 'lightgrey'
    window.add(die7, wafer.x+(window.width-wafer.x)*0.5+90, wafer.y+200)
    die8 = GRect(die_size, die_size)
    die8.filled = True
    die8.fill_color = 'lightgrey'
    window.add(die8, wafer.x+(window.width-wafer.x)*0.5+90, wafer.y+290)
    die9 = GRect(70, 70)
    die9.filled = True
    die9.fill_color = 'lightgrey'
    window.add(die9, wafer.x+(window.width-wafer.x)*0.5+175, wafer.y+205)
    
    die10 = GRect(die_size, die_size)
    die10.filled = True
    die10.fill_color = 'lightgrey'
    window.add(die10, wafer.x+(window.width-wafer.x)*0.5-die_size, wafer.y+20)
    die11 = GRect(die_size, die_size)
    die11.filled = True
    die11.fill_color = 'lightgrey'
    window.add(die11, wafer.x+(window.width-wafer.x)*0.5-die_size, wafer.y+110)
    die12 = GRect(die_size, die_size)
    die12.filled = True
    die12.fill_color = 'lightgrey'
    window.add(die12, wafer.x+(window.width-wafer.x)*0.5-die_size, wafer.y+200)
    die13 = GRect(die_size, die_size)
    die13.filled = True
    die13.fill_color = 'lightgrey'
    window.add(die13, wafer.x+(window.width-wafer.x)*0.5-die_size, wafer.y+290)
    die14 = GRect(die_size, die_size)
    die14.filled = True
    die14.fill_color = 'lightgrey'
    window.add(die14, wafer.x+(window.width-wafer.x)*0.5-die_size, wafer.y+380)
    die15 = GRect(die_size, die_size)
    die15.filled = True
    die15.fill_color = 'lightgrey'
    window.add(die15, wafer.x+(window.width-wafer.x)*0.5-2*die_size-5, wafer.y+110)
    die16 = GRect(die_size, die_size)
    die16.filled = True
    die16.fill_color = 'lightgrey'
    window.add(die16, wafer.x+(window.width-wafer.x)*0.5-2*die_size-5, wafer.y+200)
    die17 = GRect(die_size, die_size)
    die17.filled = True
    die17.fill_color = 'lightgrey'
    window.add(die17, wafer.x+(window.width-wafer.x)*0.5-2*die_size-5, wafer.y+290)
    die18 = GRect(70, 70)
    die18.filled = True
    die18.fill_color = 'lightgrey'
    window.add(die18, wafer.x+(window.width-wafer.x)*0.5-3*die_size, wafer.y+205)

    # to make inverter
    o1 = GOval(50,50)
    o1.filled = False
    o1.color = 'black'
    window.add(o1, wafer.x-300, wafer.y+50)
    line1 = GLine(wafer.x-300, wafer.y+100, wafer.x-300, wafer.y+50)
    window.add(line1)
    line1_1 = GLine(wafer.x-250, wafer.y+75, wafer.x-200, wafer.y+75)
    window.add(line1_1)
    line1_2 = GLine(wafer.x-300, wafer.y+60, wafer.x-350, wafer.y+60)
    window.add(line1_2)
    line1_3 = GLine(wafer.x-300, wafer.y+90, wafer.x-350, wafer.y+90)
    window.add(line1_3)
    line1_4 = GLine(wafer.x-350, wafer.y+60, wafer.x-350, wafer.y)
    window.add(line1_4)
    o2 = GOval(50,50)
    o2.filled = True
    o2.fill_color = 'black'
    window.add(o2, wafer.x-300, wafer.y+200)
    line2 = GLine(wafer.x-300, wafer.y+250, wafer.x-300, wafer.y+200)
    window.add(line2)
    line2_1 = GLine(wafer.x-250, wafer.y+225, wafer.x-200, wafer.y+225)
    window.add(line2_1)
    line2_2 = GLine(wafer.x-300, wafer.y+210, wafer.x-350, wafer.y+210)
    window.add(line2_2)
    line2_3 = GLine(wafer.x-300, wafer.y+240, wafer.x-350, wafer.y+240)
    window.add(line2_3)
    line2_4 = GLine(wafer.x-350, wafer.y+240, wafer.x-350, wafer.y+300)
    window.add(line2_4)

    line3 = GLine(wafer.x-200, wafer.y+75, wafer.x-200, wafer.y+225)
    window.add(line3)
    line4 = GLine(wafer.x-200, wafer.y+150, wafer.x-100, wafer.y+150)
    window.add(line4)
    line5 = GLine(wafer.x-350, wafer.y+210, wafer.x-350, wafer.y+90)
    window.add(line5)
    line_out = GLine(wafer.x-350, wafer.y+150, wafer.x-450, wafer.y+150)
    window.add(line_out)
    line6 = GLine(wafer.x-375, wafer.y, wafer.x-325, wafer.y)
    window.add(line6)
    line7 = GLine(wafer.x-375, wafer.y+300, wafer.x-325, wafer.y+300)
    window.add(line7)

    input_label = GLabel("Vin")
    input_label.font= '-40'
    window.add(input_label, wafer.x-100, wafer.y+150)

    output_label = GLabel("Vout")
    output_label.font= '-40'
    window.add(output_label, wafer.x-500, wafer.y+150)

    vdd_label = GLabel("Vdd")
    vdd_label.font= '-40'
    window.add(vdd_label, wafer.x-375, wafer.y)

    vss_label = GLabel("Vss")
    vss_label.font= '-40'
    window.add(vss_label, wafer.x-375, wafer.y+350)

    title_label = GLabel("TSMC Design Platform")
    title_label.font = 'Courier-50'
    title_label.color = 'tomato'
    window.add(title_label, x=20, y=title_label.height+10)


if __name__ == '__main__':
    main()
