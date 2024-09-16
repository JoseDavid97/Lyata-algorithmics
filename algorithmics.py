from pcolors import PCOLORS
    

class AlgorithmicsTest:
    
    __check_input_counter = 3
    __check_flag = False
    
    def __reset_fails(self):
        self.__check_flag = False
        self.__check_input_counter = 3
        
    def __log_attempts(self, msg):
        self.__check_input_counter -= 1
        
        print(PCOLORS.FAIL+msg)
        print(f"{self.__check_input_counter} intento{'s' if self.__check_input_counter!=1 else ''} restante{'s' if self.__check_input_counter!=1 else ''}\n")
        
        if not self.__check_input_counter: exit()
    
    def __check_input(self, type='int', listLength = None): 
        inputVar = input(PCOLORS.BOLD+"Entrada: ").strip()
        
        outputVar = 0
        if type == 'int':
            try:
                outputVar = int(inputVar)
                self.__check_flag = True
            except:
                if inputVar != "":
                    self.__log_attempts("Dato de entrada no es un número entero")
                else:
                    self.__check_flag = True
                    
        else:
            outputAux = inputVar.split(' ')
            outputVarL = len(outputAux)
            
            if listLength and outputVarL != listLength:
                self.__log_attempts(f"Debe ingresar {listLength} números enteros, {outputVarL} {'fueron ingresados' if outputVarL!=1 else 'fue ingresado'}")
            
            else:  
                try:
                    outputVar = [int(num) for num in outputAux]
                    self.__check_flag = True
                except:
                    self.__log_attempts("Debe ingresar solo números enteros en la lista")
                    
        print(PCOLORS.RESET, end="")
        return outputVar
                
    def get_test_list_len(self):
        print("\nA continuación, ingrese el tamaño de la lista de evaluación\nNota: Dejar en blanco si desea ingresar una lista libre\n")
        
        while (not self.__check_flag and self.__check_input_counter):
            test_list_len = self.__check_input()
            
        self.__reset_fails()
            
        return test_list_len
    
    def get_test_list(self, quantity = 0):
        print("\nA continuación, ingrese la lista de evaluación\nNota: Debe igresar números enteros separados con un espacio simple\n")
        
        while (not self.__check_flag and self.__check_input_counter):
            test_list = self.__check_input(type = 'list', listLength = quantity)
            
        self.__reset_fails()
        
        return test_list
    
    def get_query_list_len(self):
        print("\nA continuación, ingrese el tamaño de la lista de consultas\nNota: Dejar en blanco si desea ingresar una lista libre\n")
        
        while (not self.__check_flag and self.__check_input_counter):
            query_list_len = self.__check_input()
            
        self.__reset_fails()
            
        return query_list_len
    
    def get_query_list(self, quantity = 0):
        print("\nA continuación, ingrese la lista de consultas\nNota: Debe igresar números enteros separados con un espacio simple\n")
        
        while (not self.__check_flag and self.__check_input_counter):
            query_list = self.__check_input(type = 'list', listLength = quantity)
            
        self.__reset_fails()
        
        return query_list
    
    def check_borders(self, test_list, query_list):
        
        min_tl = min(test_list)
        max_tl = max(test_list)
        borders = []
        for queryNum in query_list:
            if min_tl>= queryNum:
                b0 = 'X'
            else:
                lowerBorder = min_tl
                for testNumber in test_list:
                    if testNumber > lowerBorder and testNumber < queryNum:
                        lowerBorder = testNumber
                b0 = lowerBorder
            
            if max_tl <= queryNum:
                b1 = 'X'
            else:
                upperBorder = max_tl
                for testNumber in test_list:
                    if testNumber < upperBorder and testNumber > queryNum:
                        upperBorder = testNumber
                b1 = upperBorder
            
            borders.append([b0, b1])
            
        return borders
        
    def exec(self):
        print(PCOLORS.RESET, end="")
        
        test_list_len = self.get_test_list_len()
        test_list = self.get_test_list(quantity = test_list_len if test_list_len else None)
        
        query_list_len = self.get_query_list_len()
        query_list = self.get_query_list(quantity = query_list_len if query_list_len else None)
        
        bordersList = self.check_borders(test_list, query_list)
        
        for b0, b1 in bordersList:
            print(b0, b1)