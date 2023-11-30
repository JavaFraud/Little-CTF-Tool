import curses
import file_list
import file_signatures as fs
import os
import timestamps_patterns as tsp
def main(stdscr):

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_BLACK, curses.COLOR_YELLOW)
    
    list_of_files = file_list.get_file_list(os.getcwd())
    current_option = 0
    stdscr.clear()

    files_win = curses.newwin(15,30,4,0)
    info_win = curses.newwin(20,50,4,40)
    navbar_win = curses.newwin(3,60,0,0)

    while True:
        stdscr.refresh()
        files_win.clear()
        navbar_win.clear()
#------------------------------NAV BAR-----------------------------------

        navbar_win.addstr(0,0,""" ____________________________
|      MY LITTLE CTF TOOL    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""",curses.color_pair(2)+curses.A_BOLD)
        navbar_win.refresh()

#------------------------------FILES LIST-----------------------------------

        for i, file in enumerate(list_of_files):
            if i == current_option:
                files_win.addstr(i+2,0,file, curses.color_pair(4))
            else:
                files_win.addstr(i+2,0,file,curses.color_pair(1))
        files_win.addstr(0,0,"---Files list---",curses.color_pair(3))
        files_win.refresh()

#------------------------------FILES INFORMATION-----------------------------------

        info_win.clear()
        file_sigs_info = fs.get_information(list_of_files[current_option])
        file_timestamps_info = tsp.get_timestamps_patterns_info(list_of_files[current_option])
        info_win.addstr(0, 0, "---File metadatas---",curses.color_pair(3))
        info_win.addstr(2, 0, file_timestamps_info)
        info_win.addstr(8, 0, "---File Type Informations---",curses.color_pair(3))
        info_win.addstr(10, 0, file_sigs_info)
        info_win.refresh()

#------------------------------KEY GETTING-----------------------------------

        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(list_of_files) - 1:
            current_option += 1
        elif key == curses.KEY_RIGHT:
            print("right key")
        elif key == 27:
            break

if __name__ == "__main__":
    curses.wrapper(main)