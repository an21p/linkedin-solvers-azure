import azure.functions as func
from azure.storage.blob import BlobServiceClient

from logging import debug, error
from os import getenv
from datetime import datetime

from .solver import Solver

queens_solver = func.Blueprint()

@queens_solver.function_name(name="QueensSolverTrigger")
@queens_solver.route(route="queens", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def queens_solver_trigger(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Read the image from the POST body
        image = req.get_body()
        if not image:
            return func.HttpResponse("No image providd", status_code=400)

        solved_at = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

        # Process the image using the solver
        solver = Solver(image)
        solved_at = datetime.strftime(datetime.now(), "%Y-%m-%d-%H:%M:%S.%f")
        input, solution = solver.solve()
        if solution is None:
            error("Solver failed to generate a solution")
            return func.HttpResponse("Failed to generate solution", status_code=500)

        container_name = "images"
        conn_str = getenv("linkedinsolvers_STORAGE")
        if not conn_str:
            error("linkedinsolvers_STORAGE is not set")
            return func.HttpResponse("Storage not connected", status_code=500)


        blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        container_client = blob_service_client.get_container_client(container_name)
        try:
            container_client.create_container()
        except Exception as e:
            debug(f"Container already exists or failed to create: {e}")
        
        # Upload the original image to blob name: input/{name}
        original_blob_name = f"{solved_at}_0_original.png"
        container_client.upload_blob(original_blob_name, image, overwrite=True)

        input_blob_name = f"{solved_at}_1_input.png"
        container_client.upload_blob(input_blob_name, input, overwrite=True)

        # Upload the solution to blob name: output/{solved_at}
        # If solution is not of type bytes, convert it appropriately (here assumed string)
        output_blob_name = f"{solved_at}_2_output.png"
        container_client.upload_blob(output_blob_name, solution, overwrite=True)

        return func.HttpResponse(solution, status_code=200, mimetype="image/png")
    except Exception as e:
        error(f"Error processing request: {e}")
        return func.HttpResponse("Error processing image", status_code=500)
