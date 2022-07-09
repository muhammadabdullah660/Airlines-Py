import os


class MenuUI:
    @staticmethod
    def header():
        os.system('clear')
        print(
            '------------------------------------------------------------------------------------------------------------- ')
        print(
            '                                                                                                              |')
        print(
            '|  ********  *******  *     *       ********  *****  ******   *       *****   *       *  *******   ********   |')
        print(
            '|  *      *  *     *  *   *         *      *    *    *    *   *         *     * *     *  *         *          |')
        print(
            '|  ********  *******  * **          * **** *    *    *  **    *         *     *   *   *  ******    ********   |')
        print(
            '|  *         *     *  *    *        *      *    *    *    *   *         *     *     * *  *                *   |')
        print(
            '|  *         *     *  *      *      *      *  *****  *     *  *******  *****  *       *  *******   ********   |')
        print(
            ' ------------------------------------------------------------------------------------------------------------- ')

    # MAIN MENU
    @staticmethod
    def mainMenu():
        option = 0
        print('Main Menu ')
        print('---------------------')
        print('Select one of the following options...')

        print('1- Login')
        print('2- Sign Up')
        print('3- Details')
        print('4- Exit')
        option = int(input('Your Option..'))
        return option
