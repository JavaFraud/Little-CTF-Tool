import curses
import file_list
import file_signatures as fs
import os

def main(stdscr):

    file_sigs_json_path = os.getcwd()+'\\'+'file_sigs.json'
    file_sigs = fs.get_file_sigs_from_json(file_sigs_json_path)

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    list_of_files = file_list.get_file_list(os.getcwd())
    current_option = 0
    result_is_asked = False
    while True:
        stdscr.addstr(0, 0, "─"*13+" FILE INFORMATIONS "+"─"*14, curses.color_pair(2))
        stdscr.addstr(0, 46, "╮", curses.color_pair(2))
        for i, file in enumerate(list_of_files):
            stdscr.addstr(i+1, 46, "│", curses.color_pair(2))
            stdscr.addstr(i+2, 46, "│", curses.color_pair(2))
            if i == current_option:
                stdscr.addstr(i+2, 50, file, curses.A_REVERSE)
            else:
                stdscr.addstr(i+2, 50, file)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(list_of_files) - 1:
            current_option += 1
        elif key == curses.KEY_RIGHT:
            stdscr.clear()
            file_to_analyse_hex = fs.read_file_hex(list_of_files[current_option])
            file_sigs_info = fs.get_file_header_info(file_to_analyse_hex, file_sigs)
            stdscr.addstr(2, 0, file_sigs_info)
            stdscr.refresh()
            print("Right pressed")
            
        elif key == 27:  # 27 est la valeur ASCII pour la touche Échap, sortir de la boucle si Échap est pressé
            break

if __name__ == "__main__":
    curses.wrapper(main)