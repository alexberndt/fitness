from fastapi import FastAPI

from app.models.exercise import Exercise, Muscle

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/exercises")
async def exercises():
    # Return the list of exercises in the database
    exercises = [
        Exercise(
            id="1",
            name="Push-up",
            description="A push-up is a common calisthenics exercise beginning from the prone position. By raising and lowering the body using the arms, push-ups exercise the pectoral muscles, triceps, and anterior deltoids, with ancillary benefits to the rest of the deltoids, serratus anterior, coracobrachialis and the midsection as a whole.",
            target_muscles=[
                Muscle(id="1", name="Pectoralis Major"),
                Muscle(id="2", name="Triceps Brachii"),
                Muscle(id="3", name="Deltoid"),
            ],
        ),
        Exercise(
            id="2",
            name="Pull-up",
            description="A pull-up is an upper-body strength exercise. The pull-up is a closed-chain movement where the body is suspended by the hands and pulls up. As this happens, the elbows flex and the shoulders adduct and extend to bring the elbows to the torso.",
            target_muscles=[
                Muscle(id="4", name="Latissimus Dorsi"),
                Muscle(id="5", name="Biceps Brachii"),
                Muscle(id="6", name="Teres Major"),
            ],
        ),
    ]
    return {"exercises": exercises}


@app.get("/muscles")
async def muscles():
    # Return the list of muscles in the database
    muscles = [
        Muscle(id="1", name="Pectoralis Major"),
        Muscle(id="2", name="Triceps Brachii"),
        Muscle(id="3", name="Deltoid"),
        Muscle(id="4", name="Latissimus Dorsi"),
        Muscle(id="5", name="Biceps Brachii"),
        Muscle(id="6", name="Teres Major"),
    ]
    return {"muscles": muscles}
