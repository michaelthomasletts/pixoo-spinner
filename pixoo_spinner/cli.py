#!/usr/bin/env python3

__all__ = ["run"]

from click import Tuple, command, option

from .spinner import PixooSpinner


@command()
@option(
    "--ip",
    "-i",
    type=str,
    required=True,
    prompt="The IP address for Pixoo device",
    help="The IP address for Pixoo device",
)
@option(
    "--imageloc",
    "-il",
    type=str,
    required=True,
    prompt="Where the base image is stored",
    help="Where the base image is stored",
)
@option(
    "--screensize",
    "-ss",
    type=Tuple([int, int]),
    required=False,
    help="The size of your LED screen",
    default=(64, 64),
)
@option(
    "--fps",
    "-f",
    type=float,
    required=False,
    help="Frames per second",
    default=0.1,
)
@option(
    "--rotation",
    "-r",
    type=str,
    help="Which way the image rotates",
    default="right",
)
@option(
    "--degreerotation",
    "-dr",
    type=int,
    help="How many degrees the image rotates at a time",
    default=5,
)
@option(
    "--gradiatecolors", "-gc", type=bool, help="Whether or not to gradiate the color slowly", default=True
)
@option(
    "--testing",
    "-t",
    type=bool,
    help="Are you testing locally?",
    default=False,
)
def run(
    ip,
    imageloc,
    screensize,
    fps,
    rotation,
    degreerotation,
    gradiatecolors,
    testing,
):
    app = PixooSpinner(
        ip_address=ip,
        image_loc=imageloc,
        screen_size=screensize,
        fps=fps,
        rotation=rotation,
        degree_rotation=degreerotation,
        gradiate_colors=gradiatecolors,
        testing=testing,
    )
    app.spin()


if __name__ == "__main__":
    run()
