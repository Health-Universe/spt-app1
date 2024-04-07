"""

"""
import os
from typing import Optional
from PIL import Image


def convert_video(
    video_in: str,
    video_out: str,
    scale: Optional[str],
):
    """Convert videos to H264 codec for HTML5 video player.

    scale: 2000:-1

    :return:
    """
    print(f"{video_in} -> {video_out}")
    scale_str = f"scale={scale} " if scale else ""
    command = f"ffmpeg -y -i {video_in} -vf {scale_str}-vcodec libx264 -preset slow -crf 18 {video_out}"

    print(command)
    os.system(command)


def convert_image(
    image_in: str,
    image_out: str,
    width: int,
    dpi: int = 150

):
    print(f"{image_in} -> {image_out}")
    im = Image.open(image_in)
    width_start, height_start = im.size
    height = int(height_start * width/width_start)
    im_resized = im.resize(size=(width, height))
    im_resized.save(image_out, dpi=(dpi, dpi))


if __name__ == "__main__":

    for k in range(1, 49):
        # convert_video(
        #     video_in=f"sim{k:>03}_200_86400.0.mp4",
        #     video_out=f"sim{k:>03}_h264.mp4",
        # )
        # convert_video(
        #     video_in=f"sim{k:>03}_h264.mp4",
        #     video_out=f"sim{k:>03}_h264.mp4",
        #     scale="2000:-1"
        # )
        convert_image(
            image_in=f"sim{k:>03}_10_86400.0.png",
            image_out=f"sim{k:>03}.png",
            width=2000,
            dpi=150
        )

