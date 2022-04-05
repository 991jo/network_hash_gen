from typing import Optional
import random


def _generate_salt(chars: str, length: int, seed: Optional[str] = None) -> str:
    """
    Generates a salt with the specified `length`, chosen randomly from the
    charaters in `chars`

    If `seed` is specified the value is used to initialize the random number
    generator.
    """

    # initialize a seperate RNG to no seed the global instance used by the
    # functions called directly on the random module.
    rng = random.Random()

    if seed is not None:
        rng.seed(seed)

    output = ""
    for _ in range(length):
        output += rng.choice(chars)

    return output
