import azure.functions as func

bp = func.Blueprint() 

@bp.route(route="Voorbeeld_functie", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def Voorbeeld_functie(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("De voorbeeldfunctie werkte", status_code=200)