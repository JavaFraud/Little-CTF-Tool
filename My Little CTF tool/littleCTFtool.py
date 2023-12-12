import curses
import file_list
import file_signatures as fs
import os
import timestamps_patterns as tsp
import platform

def path_type_configuration():
    if platform.system() == "Linux":
        configuration = "/"
    if platform.system() == "Windows":
        configuration = "\\"
    return configuration

def init_color_pairs(curses):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)

def navbar_display(navbar, file, dirs):
    navbar.addstr(0,0," |      MY LITTLE CTF TOOL    |",curses.color_pair(2)+curses.A_REVERSE)
    navbar.addstr(1,0,"Working in : "+dirs,curses.color_pair(2))
    navbar.addstr(2,0,"Working on : "+file,curses.color_pair(2))
    navbar.addstr(3,0,"↔↕: navigate / a: access dir / h: display help /f: access file-signature tool / s: access steganography tool",curses.color_pair(6))

def list_displayer(curses,some_pad,some_list,some_y_list_index,dir0file1,dirOrfile01,current_option,name):

    for i, file in enumerate(some_list):
        if i == current_option and dir0file1 == dirOrfile01:
            some_pad.addstr(i+2,0,file, curses.color_pair(4))
        else:
            some_pad.addstr(i+2,0,file,curses.color_pair(1))

    #Top border
    some_pad.addstr(some_y_list_index,0,"----"+name+" list----",curses.color_pair(3))
    some_pad.addstr(some_y_list_index,17,"            ",curses.color_pair(1))

    #Srolling informations
    if some_y_list_index != 0:
        some_pad.addstr(some_y_list_index+1,0,"------ ↑↑↑ ------",curses.color_pair(5))
        some_pad.addstr(some_y_list_index+1,17,"             ",curses.color_pair(1))
    if current_option != len(some_list)-1 and len(some_list) >= 13 and some_y_list_index != len(some_list)-14:
        some_pad.addstr(some_y_list_index+16,0,"------ ↓↓↓ ------",curses.color_pair(5))
    else:
        some_pad.addstr(some_y_list_index+16,0,"=================",curses.color_pair(3))
    some_pad.addstr(some_y_list_index+16,17,"                       ",curses.color_pair(1))

def informations_displayer(curses,info_win,file_sigs_info,file_timestamps_info):
    info_win.addstr(0, 0, "---File metadatas---",curses.color_pair(3))
    info_win.addstr(2, 0, file_timestamps_info)
    info_win.addstr(8, 0, "---File Type Informations---",curses.color_pair(3))
    info_win.addstr(10, 0, file_sigs_info)

def update_lists(current_dir):
    elements = file_list.get_file_list(current_dir)
    list_of_files = elements["files"]
    list_of_dirs = elements["dirs"]
    list_of_dirs.insert(0,"..")
    return list_of_files, list_of_dirs

def up_down(key,curses,current_x_option,y_x_list_index,list_lenght):
    print("inside")
    if key == curses.KEY_UP and current_x_option > 0:
        #Scrolling list management
        if current_x_option == y_x_list_index:
            y_x_list_index += -1
        current_x_option -= 1

    elif key == curses.KEY_DOWN and current_x_option < list_lenght - 1:
        if current_x_option - 1 == y_x_list_index + 12:
            y_x_list_index += 1
        current_x_option += 1

def main(stdscr):

#------------------------------INITIALISATION----------------------------

    path_type = path_type_configuration()
    filesigs_path = os.path.dirname(os.path.abspath(__file__))+path_type+"file_sigs.json"
    timestamps_path = os.path.dirname(os.path.abspath(__file__))+path_type+"timestamps_patterns.json"
    current_dir = os.getcwd()
    list_of_files,list_of_dirs = update_lists(current_dir)
    current_file_option = 0
    current_dir_option = 0
    dir0file1 = 1
    y_dir_list_index = 0
    y_file_list_index = 0

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    init_color_pairs(curses)

    navbar_win = curses.newwin(4,120,0,0)
    info_win = curses.newwin(20,50,4,70)
    files_pad = curses.newpad(100,60)
    dirs_pad = curses.newpad(100,30)

    while True:

        #clear
        stdscr.refresh()
        navbar_win.clear()        
        files_pad.clear()
        dirs_pad.clear()
        info_win.clear()

        #nav
        navbar_display(navbar_win,list_of_files[current_file_option],os.getcwd())
        navbar_win.refresh()

        #dirs
        list_displayer(curses,dirs_pad,list_of_dirs,y_dir_list_index,dir0file1,0,current_dir_option,"Dirs")
        dirs_pad.refresh(y_dir_list_index,0,4,0,20,30)

        #files
        list_displayer(curses,files_pad,list_of_files,y_file_list_index,dir0file1,1,current_file_option,"Files")
        files_pad.refresh(y_file_list_index,0,4,30,20,60)
        
        #informations
        file_sigs_info = fs.get_information(current_dir + path_type + list_of_files[current_file_option], filesigs_path)
        file_timestamps_info = tsp.get_timestamps_patterns_info(current_dir + path_type + list_of_files[current_file_option],timestamps_path)
        informations_displayer(curses,info_win,file_sigs_info,file_timestamps_info)
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
            #up_down(key,curses,current_dir_option,y_dir_list_index,len(list_of_dirs))
            if key == curses.KEY_RIGHT:
                dir0file1 = 1
                current_file_option = 0

            elif key == ord('a'):
                if current_dir_option == 0:
                    try:
                        os.chdir(os.getcwd()+path_type+"..")
                    except:
                        print("err")
                else:
                    os.chdir(os.getcwd() + path_type + list_of_dirs[current_dir_option])
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