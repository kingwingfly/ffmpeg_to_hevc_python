import os
import shutil


def to_hevc(path_in):
    it = os.walk(path_in)
    for dirpath, _, filenames in it:
        for video in filenames:
            src_format = [".mp4", ".avi", ".flv", ".mov", ".mkv"]
            flag = False
            for ft in src_format:
                if video.endswith(ft):
                    flag = True
                    break
            if not flag:
                print(f"{video} is not a video.")
                continue
            path_out = dirpath + "_out"
            print(f"output: {path_out}")
            if not os.path.exists(path_out):
                os.mkdir(path_out)
            print(f"《{video}》 start\n" + "=" * 10)

            video_path_in = os.path.join(dirpath, video)
            video_path_out = os.path.join(
                path_out, "".join(video.split(".")[:-1:]) + ".mp4"
            )

            order = f'ffmpeg -y -i "{video_path_in}" -c:v hevc_nvenc -preset slow "{video_path_out}"'
            print(order)
            os.system(order)
            print(f"《{video}》 Finished\n" + "=" * 10)
            size_in = os.path.getsize(video_path_in)
            size_out = os.path.getsize(video_path_out)
            if size_in >= size_out:
                os.remove(video_path_in)
                continue
            os.remove(video_path_out)
            shutil.move(video_path_in, video_path_out)
        print(f"{dirpath} Finished\n" + "=" * 15)
    print(f"{path_in} ALL FINISH\n" + "=" * 15)


def clear(path):
    it = os.walk(path)
    for dirpath, dirnames, filenames in it:
        if dirnames == [] and filenames == []:
            os.rmdir(dirpath)
            print(f"Empty dir {dirpath} deleted.")


if __name__ == "__main__":
    paths = ["E:\Videos"]
    for path in paths:
        to_hevc(path)
        clear(path)
    print("ALL FINISH!!!")
