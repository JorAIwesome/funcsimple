import azure.functions as func
from Functies.Voorbeeld_functie import bp as Voorbeeld_bp

app = func.FunctionApp()

# Initialiseer de fucnties uit de blueprint in de fucntion app
app.register_functions(Voorbeeld_bp)

# Funcite die kan worden gebruikt om te testen of functieapp draaiend is
@app.function_name(name="test")
@app.route(route="test", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Functie app is draaiend.", status_code=200)