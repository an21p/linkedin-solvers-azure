import azure.functions as func
from Queens import queens_solver

app = func.FunctionApp()

app.register_functions(queens_solver)
