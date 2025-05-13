__all__ = ["PixooSpinner"]

import time
import tkinter as tk
from pathlib import Path
from typing import Literal, Tuple

from PIL import Image, ImageTk
from pixoo1664 import Pixoo


class PixooSpinner:
    def __init__(
        self,
        image_loc: str,
        ip_address: str,
        screen_size: Tuple[int, int] = (64, 64),
        fps: float = 0.1,
        rotation: Literal["left", "right"] = "right",
        degree_rotation: int = 5,
        gradiate_colors: bool = True,
        testing: bool = False,
    ):
        self.ip_address = ip_address
        self.image_loc = image_loc
        self.screen_size = screen_size
        self.fps = fps
        self.fps_ms = int(self.fps * 1000)
        self.testing = testing

        if not testing:
            self.pixoo = Pixoo(self.ip_address)
        else:
            self.pixoo = None

        self.base_image = (
            Image.open(self.image_loc).convert("RGBA").resize(self.screen_size)
        )
        self.background = Image.new("RGB", self.screen_size, (0, 0, 0))
        self.angle = 0
        self.rotation = rotation
        self.degree_rotation = degree_rotation
        self.gradiate_colors = gradiate_colors
        self.orientation = (
            (self.angle + self.degree_rotation)
            if self.rotation == "left"
            else (self.angle - self.degree_rotation)
        )
        self.color = (255, 0, 0)
        self.gradient_phase = 0

    def spin(self):
        if not self.testing:
            while True:
                if self.gradiate_colors:
                    self.increment_rgb()
                    symbol = self.recolor(self.base_image)
                    rotated = symbol.rotate(
                        self.angle, resample=Image.BICUBIC, expand=True
                    )
                else:
                    rotated = self.base_image.rotate(
                        self.angle, resample=Image.BICUBIC, expand=True
                    )

                composite = self.background.copy()
                offset = (
                    (64 - rotated.width) // 2,
                    (64 - rotated.height) // 2,
                )
                composite.paste(rotated, offset, rotated)
                self.pixoo.send_image(composite)

                # setting angle N degrees
                self.increment_angle()
                time.sleep(self.fps)
        else:
            self.simulate()

    def increment_angle(self):
        self.angle = (
            self.angle - self.degree_rotation
            if self.rotation == "right"
            else self.angle + self.degree_rotation
        ) % 360

    def increment_rgb(self):
        r, g, b = self.color
        step = 1  # can be increased for faster transitions

        if self.gradient_phase == 0:  # R → Y
            g = min(255, g + step)
            if g == 255:
                self.gradient_phase = 1
        elif self.gradient_phase == 1:  # Y → G
            r = max(0, r - step)
            if r == 0:
                self.gradient_phase = 2
        elif self.gradient_phase == 2:  # G → C
            b = min(255, b + step)
            if b == 255:
                self.gradient_phase = 3
        elif self.gradient_phase == 3:  # C → B
            g = max(0, g - step)
            if g == 0:
                self.gradient_phase = 4
        elif self.gradient_phase == 4:  # B → M
            r = min(255, r + step)
            if r == 255:
                self.gradient_phase = 5
        elif self.gradient_phase == 5:  # M → R
            b = max(0, b - step)
            if b == 0:
                self.gradient_phase = 0

        self.color = (r, g, b)

    def recolor(self, image: Image.Image) -> Image.Image:
        r, g, b = self.color
        data = [(r, g, b, a) for _, _, _, a in image.getdata()]
        recolored = Image.new("RGBA", image.size)
        recolored.putdata(data)
        return recolored

    def simulate(self):
        frames: int = 255 * 6
        root = tk.Tk()
        root.title("Simulated Spin")
        label = tk.Label(root)
        label.pack()

        def update(frame_count=[0]):
            # destroy app when gradient has finished running
            if frame_count[0] >= frames:
                root.destroy()
                return

            if self.gradiate_colors:
                self.increment_rgb()
                symbol = self.recolor(self.base_image)
                rotated = symbol.rotate(
                    self.angle, resample=Image.BICUBIC, expand=True
                )
            else:
                rotated = self.base_image.rotate(
                    self.angle, resample=Image.BICUBIC, expand=True
                )

            offset = (
                (self.screen_size[0] - rotated.width) // 2,
                (self.screen_size[1] - rotated.height) // 2,
            )
            composite = self.background.copy()
            composite.paste(rotated, offset, rotated)
            tk_img = ImageTk.PhotoImage(composite)
            label.configure(image=tk_img)
            label.image = tk_img
            self.increment_angle()
            frame_count[0] += 1
            root.after(self.fps_ms, update)

        update()
        root.mainloop()
