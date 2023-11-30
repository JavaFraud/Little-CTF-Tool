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

#------------------------------PATH MANAGEMENT---------------------------

    current_dir = os.getcwd()
    relativ_path = "\\testFolder"
    folderpath = current_dir + relativ_path
    fancy_relativ_path = ".\\" + relativ_path + "\\"
    
    elements = file_list.get_file_list(folderpath)
    list_of_files = elements["files"]
    list_of_dirs = elements["dirs"]
    current_file_option = 0
    current_dir_option = 0
    dir0file1 = 0
    stdscr.clear()

#------------------------------WINDOWS CREATION--------------------------

    navbar_win = curses.newwin(3,80,0,0)
    dirs_win = curses.newwin(25,30,4,0)
    files_win = curses.newwin(25,30,4,30)
    info_win = curses.newwin(20,50,4,70)

    while True:
        stdscr.refresh()
        files_win.clear()
        navbar_win.clear()
#------------------------------NAV BAR-----------------------------------

        navbar_win.addstr(0,0," |      MY LITTLE CTF TOOL    |",curses.color_pair(2)+curses.A_REVERSE)
        navbar_win.addstr(1,0,"Working in : "+os.getcwd(),curses.color_pair(2))
        navbar_win.addstr(2,0,"Working on : "+list_of_files[current_file_option],curses.color_pair(2))
        navbar_win.refresh()

#------------------------------DIRS List---------------------------

        for i, directory in enumerate(list_of_dirs):
            if i == current_file_option:
                dirs_win.addstr(i+2,0,directory, curses.color_pair(4))
            else:
                dirs_win.addstr(i+2,0,directory,curses.color_pair(1))
        dirs_win.addstr(0,0,"---Dirs list---",curses.color_pair(3))
        dirs_win.refresh()

#------------------------------FILES LIST--------------------------------

        for i, file in enumerate(list_of_files):
            if i == current_file_option:
                files_win.addstr(i+2,0,file, curses.color_pair(4))
            else:
                files_win.addstr(i+2,0,file,curses.color_pair(1))
        files_win.addstr(0,0,"---Files list---",curses.color_pair(3))
        files_win.refresh()

#------------------------------FILES INFORMATION-------------------------

        info_win.clear()
        file_sigs_info = fs.get_information(fancy_relativ_path + list_of_files[current_file_option])
        file_timestamps_info = tsp.get_timestamps_patterns_info(fancy_relativ_path + list_of_files[current_file_option])
        info_win.addstr(0, 0, "---File metadatas---",curses.color_pair(3))
        info_win.addstr(2, 0, file_timestamps_info)
        info_win.addstr(8, 0, "---File Type Informations---",curses.color_pair(3))
        info_win.addstr(10, 0, file_sigs_info)
        info_win.refresh()

#------------------------------KEY GETTING-------------------------------

        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_file_option > 0:
            current_file_option -= 1
        elif key == curses.KEY_DOWN and current_file_option < len(list_of_files) - 1:
            current_file_option += 1
        elif key == curses.KEY_RIGHT:
            print("right key")
        elif key == 27:
            print(os.getcwd()+"\\testFolder")
            break

if __name__ == "__main__":
    curses.wrapper(main)