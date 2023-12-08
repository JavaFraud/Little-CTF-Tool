import curses
import file_list
import file_signatures as fs
import os
import timestamps_patterns as tsp

def update_lists(current_dir):
    elements = file_list.get_file_list(current_dir)
    list_of_files = elements["files"]
    list_of_dirs = elements["dirs"]
    list_of_dirs.insert(0,"..")
    return list_of_files, list_of_dirs


def main(stdscr):

    filesigs_path = os.path.dirname(os.path.abspath(__file__))+"\\file_sigs.json"
    timestamps_path = os.path.dirname(os.path.abspath(__file__))+"\\timestamps_patterns.json"
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(5,curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(6,curses.COLOR_BLUE, curses.COLOR_BLACK)

#------------------------------PATH MANAGEMENT---------------------------

    current_dir = os.getcwd()
    
    elements = file_list.get_file_list(current_dir)

    list_of_files = elements["files"]

    list_of_dirs = elements["dirs"]
    list_of_dirs.insert(0,"..")

    current_file_option = 0
    current_dir_option = 0
    dir0file1 = 1
    stdscr.clear()

#------------------------------WINDOWS CREATION--------------------------

    navbar_win = curses.newwin(4,120,0,0)
    info_win = curses.newwin(20,50,4,70)

    files_pad= curses.newpad(100,60)
    dirs_pad= curses.newpad(100,30)

    y_dir_list_index = 0
    y_file_list_index = 0

    while True:
        stdscr.refresh()
        navbar_win.clear()

        files_pad.clear()
        dirs_pad.clear()

#------------------------------NAV BAR-----------------------------------

        navbar_win.addstr(0,0," |      MY LITTLE CTF TOOL    |",curses.color_pair(2)+curses.A_REVERSE)
        navbar_win.addstr(1,0,"Working in : "+os.getcwd(),curses.color_pair(2))
        navbar_win.addstr(2,0,"Working on : "+list_of_files[current_file_option],curses.color_pair(2))
        navbar_win.addstr(3,0,"↔↕: navigate / a: access dir / h: display help /f: access file-signature tool / s: access steganography tool",curses.color_pair(6))
        #
        navbar_win.refresh()

#------------------------------DIRS LIST---------------------------------

        for i, directory in enumerate(list_of_dirs):
            #Selection
            if i == current_dir_option and dir0file1 == 0 :
                dirs_pad.addstr(i+2,0,directory, curses.color_pair(4))
            else:
                dirs_pad.addstr(i+2,0,directory,curses.color_pair(1))
        #Top Border
        dirs_pad.addstr(y_dir_list_index,0,"----Dirs list----",curses.color_pair(3))
        dirs_pad.addstr(y_dir_list_index,17,"             ",curses.color_pair(1))

        #Srolling informations
        if y_dir_list_index != 0:
            dirs_pad.addstr(y_dir_list_index+1,0,"------ ↑↑↑ ------",curses.color_pair(5))
            dirs_pad.addstr(y_dir_list_index+1,17,"             ",curses.color_pair(1))
        if current_dir_option != len(list_of_dirs)-1 and len(list_of_dirs) >= 13 and y_dir_list_index != len(list_of_dirs)-14:
            #not working as intended when some lists are at the limit.. Gotta fix that
            dirs_pad.addstr(y_dir_list_index+16,0,"------ ↓↓↓ ------",curses.color_pair(5))
        else:
            dirs_pad.addstr(y_dir_list_index+16,0,"=================",curses.color_pair(3))
        dirs_pad.addstr(y_dir_list_index+16,17,"             ",curses.color_pair(1))

        dirs_pad.refresh(y_dir_list_index,0,4,0,20,30)

#------------------------------FILES LIST--------------------------------

        for i, file in enumerate(list_of_files):
            if i == current_file_option and dir0file1 == 1 :
                files_pad.addstr(i+2,0,file, curses.color_pair(4))
            else:
                files_pad.addstr(i+2,0,file,curses.color_pair(1))

        #Top border
        files_pad.addstr(y_file_list_index,0,"----Files list----",curses.color_pair(3))
        files_pad.addstr(y_file_list_index,17,"            ",curses.color_pair(1))

        #Srolling informations
        if y_file_list_index != 0:
            files_pad.addstr(y_file_list_index+1,0,"------ ↑↑↑ ------",curses.color_pair(5))
            files_pad.addstr(y_file_list_index+1,17,"             ",curses.color_pair(1))
        if current_file_option != len(list_of_files)-1 and len(list_of_files) >= 13 and y_file_list_index != len(list_of_files)-14:
            files_pad.addstr(y_file_list_index+16,0,"------ ↓↓↓ ------",curses.color_pair(5))
        else:
            files_pad.addstr(y_file_list_index+16,0,"=================",curses.color_pair(3))
        files_pad.addstr(y_file_list_index+16,17,"                       ",curses.color_pair(1))

        files_pad.refresh(y_file_list_index,0,4,30,20,60)

#------------------------------FILES INFORMATION-------------------------

        info_win.clear()
        file_sigs_info = fs.get_information(current_dir + "\\" + list_of_files[current_file_option], filesigs_path)
        file_timestamps_info = tsp.get_timestamps_patterns_info(current_dir + "\\" + list_of_files[current_file_option],timestamps_path)
        info_win.addstr(0, 0, "---File metadatas---",curses.color_pair(3))
        info_win.addstr(2, 0, file_timestamps_info)
        info_win.addstr(8, 0, "---File Type Informations---",curses.color_pair(3))
        info_win.addstr(10, 0, file_sigs_info)
        info_win.refresh()

#------------------------------KEY GETTING-------------------------------

        stdscr.refresh()
        key = stdscr.getch()

        if(dir0file1 == 0):

            if key == curses.KEY_UP and current_dir_option > 0:
                #Scrolling list management
                if current_dir_option == y_dir_list_index:
                    y_dir_list_index += -1
                current_dir_option -= 1

            elif key == curses.KEY_DOWN and current_dir_option < len(list_of_dirs) - 1:
                if current_dir_option - 1 == y_dir_list_index + 12:
                    y_dir_list_index += 1
                current_dir_option += 1
                
            elif key == curses.KEY_RIGHT:
                dir0file1 = 1
                current_file_option = 0

            elif key == ord('a'):
                if current_dir_option == 0:
                    try:
                        os.chdir(os.getcwd()+"\\..")
                    except:
                        print("err")
                else:
                    os.chdir(os.getcwd() + "\\" + list_of_dirs[current_dir_option])
                current_dir = os.getcwd()
                list_of_files, list_of_dirs = update_lists(current_dir)
                current_file_option = 0
                current_dir_option = 0
                dir0file1 = 0
                y_dir_list_index = 0
                
            elif key == 27:
                break

        elif(dir0file1 == 1):

            if key == curses.KEY_UP and current_file_option > 0:
                if current_file_option == y_file_list_index:
                    y_file_list_index += -1
                current_file_option -= 1
            elif key == curses.KEY_DOWN and current_file_option < len(list_of_files) - 1:
                if current_file_option -1 == y_file_list_index + 12:
                    y_file_list_index += 1
                current_file_option += 1
            elif key == curses.KEY_LEFT:
                dir0file1 = 0
                current_dir_option = 0
                y_dir_list_index = 0
        
        if key == 27:
            break

if __name__ == "__main__":
    curses.wrapper(main)