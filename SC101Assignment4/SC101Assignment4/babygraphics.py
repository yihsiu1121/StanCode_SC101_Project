"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space_between_lines = (width - 2 * GRAPH_MARGIN_SIZE) / (len(YEARS) - 1)  # calculate space between lines
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * space_between_lines  # calculate x coordinates of year index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Draw lines for top and bottom lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Draw vertical lines for each year and put text of year to the plot
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # 精簡版本，把處理2020的data和text一併處理
    # need index and name from lookup_names list so use enumerate func.-->(0, Kyle)
    for idx, name in enumerate(lookup_names):
        color = COLORS[idx % len(COLORS)]  # 利用餘數讓不同名字的index決定線條顏色

        for i in range(len(YEARS)):
            year = str(YEARS[i])

            # dict.get(key, default=None)
            # 查找特定的名字的dict.裡年分(key)和其對應的排名(value)，如果該年分數據不存在返回一個超過NAX_RANK的值
            rank = int(name_data[name].get(year, MAX_RANK + 1))
            x = get_x_coordinate(CANVAS_WIDTH, i)
            y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (rank / MAX_RANK)

            # 處理連線的部分，所以設定條件排除最後一個年份2020
            if i < len(YEARS) - 1:
                year_next = str(YEARS[i + 1])
                rank_next = int(name_data[name].get(year_next, MAX_RANK + 1))
                x_next = get_x_coordinate(CANVAS_WIDTH, i + 1)
                y_next = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (rank_next / MAX_RANK)
                canvas.create_line(x, y, x_next, y_next, width=LINE_WIDTH, fill=color)

            # 統一加上text
            canvas.create_text(x + TEXT_DX, y, text=f'{name} {rank if rank <= MAX_RANK else "*"}', anchor=tkinter.SW,
                               fill=color)

    # # need index and name from lookup_names list so use enumerate func.-->(0, Kyle)
    # for index, name in enumerate(lookup_names):
    #     color = COLORS[index % len(COLORS)]  # 利用餘數讓不同名字的index決定線條顏色
    #     if name in name_data:
    #         for i in range(len(YEARS) - 1):
    #             year = str(YEARS[i])
    #             next_year = str(YEARS[i + 1])
    #
    #             x1 = get_x_coordinate(CANVAS_WIDTH, i)
    #             x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)
    #
    #             # dict.get(key, default=None)
    #             # 查找特定的名字的dict.裡年分(key)和其對應的排名(value)，如果該年分數據不存在返回一個超過NAX_RANK的值
    #             rank1 = int(name_data[name].get(year, MAX_RANK + 1))
    #             rank2 = int(name_data[name].get(next_year, MAX_RANK + 1))
    #
    #             # CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE 是去掉上下邊距後的有效繪圖高度
    #             # rank1 / MAX_RANK 是為了將rank1標準化為一個0->1間的數值(標準化排名)
    #             # 將標準化排名乘以有效高度，得到相對於圖表頂部的像素距離
    #             y1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (rank1 / MAX_RANK)
    #             y2 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (rank2 / MAX_RANK)
    #
    #             canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
    #             canvas.create_text(x1 + TEXT_DX, y1, text=f'{name} {rank1 if rank1 <= MAX_RANK else "*"}',
    #                                anchor=tkinter.SW, fill=color)
    #
    #         # Address year 2020 data and text
    #         year = str(YEARS[-1])
    #         rank = int(name_data[name].get(year, MAX_RANK + 1))
    #         x = get_x_coordinate(CANVAS_WIDTH, len(YEARS) - 1)
    #         y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (rank / MAX_RANK)
    #         canvas.create_text(x + TEXT_DX, y, text=f'{name} {rank if rank <= MAX_RANK else "*"}', anchor=tkinter.SW,
    #                            fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
