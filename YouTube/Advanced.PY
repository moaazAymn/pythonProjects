from tkinter import messagebox
from pytube import YouTube


def Audio_H():
    YouTube(url).streams.get_audio_only("mp4").download("Audios")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Audio_1():
    YouTube(url).streams.get_by_itag(251).download("Audios")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Audio_2():
    YouTube(url).streams.get_by_itag(128).download("Audios")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Audio_3():
    YouTube(url).streams.get_by_itag(70).download("Audios")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Audio_4():
    YouTube(url).streams.get_by_itag(50).download("Audios")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Audio_5():
    YouTube(url).streams.get_by_itag(48).download("Audios")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_a_H():
    YouTube(url).streams.get_highest_resolution().download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_a_L():
    YouTube(url).streams.get_lowest_resolution().download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_a_1():
    YouTube(url).streams.get_by_itag(22).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_a_2():
    YouTube(url).streams.get_by_itag(18).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_a_3():
    YouTube(url).streams.get_by_itag(17).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_1():
    YouTube(url).streams.get_by_itag(313).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_2():
    YouTube(url).streams.get_by_itag(271).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_3():
    YouTube(url).streams.get_by_itag(248).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_4():
    YouTube(url).streams.get_by_itag(247).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_5():
    YouTube(url).streams.get_by_itag(244).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_6():
    YouTube(url).streams.get_by_itag(243).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_7():
    YouTube(url).streams.get_by_itag(242).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_webm_8():
    YouTube(url).streams.get_by_itag(278).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_mp4_1():
    YouTube(url).streams.get_by_itag(137).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_mp4_2():
    YouTube(url).streams.get_by_itag(136).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_mp4_3():
    YouTube(url).streams.get_by_itag(135).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_mp4_4():
    YouTube(url).streams.get_by_itag(134).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_mp4_5():
    YouTube(url).streams.get_by_itag(133).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


def Video_mp4_6():
    YouTube(url).streams.get_by_itag(160).download("Videos")
    messagebox.showinfo("Success", "Downloaded Successfully")


while True:

    while True:

        try:

            url = input("input youtube video url: \n")

            if (
                url.startswith("https://www.youtube.com/")
                or url.startswith("https://www.youtu.be/")
                or url.startswith("https://youtu.be/")
                or url.startswith("http://www.youtube.com/")
                or url.startswith("http://youtu.be/")
                or url.startswith("www.youtube.com/")
                or url.startswith("www.youtu.be/")
                or url.startswith("youtube.com/")
                or url.startswith("youtu.be/")
            ):
                break

            else:
                raise ValueError

        except ValueError:

            print("\ninvalid input. please enter a youtube video url\n")

    while True:

        while True:

            try:

                V_A = input(
                    "\nChoose \
\
(1) or (2):\n\
\
1- Video\n\
\
2- Audio\n"
                )

                if V_A in ("1", "2"):
                    break

                else:
                    raise ValueError

            except ValueError:
                print(
                    "\ninvalid input.\n\
\
Please enter (1) or (2)\n"
                )

        if V_A == "1":

            while True:

                while True:

                    try:

                        V = input(
                            "\nChoose (1) or (2):\n\
\
1- Video With Audio\n\
\
2- Video Without Audio\n"
                        )

                        if V in ("1", "2"):
                            break

                        else:
                            raise ValueError

                    except ValueError:

                        print(
                            "\ninvalid input.\n\
\
Please enter (1) or (2)\n"
                        )

                if V == "1":

                    while True:

                        while True:

                            try:

                                Vtype = input(
                                    "\nChoose (1) or (2) or (3):\n\
\
1- Highest Resolution\n\
\
2- Lowest Resolution\n\
\
3- Custom\n"
                                )

                                if Vtype in ("1", "2", "3"):
                                    break

                                else:
                                    raise ValueError

                            except ValueError:
                                print(
                                    "\ninvalid input.\n\
\
Please enter (1) or (2) or (3)"
                                )

                        if Vtype == "1":
                            print("...Loading")
                            Video_a_H()
                            print("\nVideo is downloaded")
                            break

                        elif Vtype == "2":
                            print("...Loading")
                            Video_a_L()
                            print("\nVideo is downloaded")
                            break

                        elif Vtype == "3":

                            while True:

                                try:

                                    V_q = input(
                                        "\nChoose (1) or (2) or (3):\n\
\
1- 720p\n\
\
2- 360p\n\
\
3- 144p\n"
                                    )

                                    if V_q in ("1", "2", "3"):
                                        break

                                    else:
                                        raise ValueError

                                except ValueError:

                                    print(
                                        "\ninvalid input.\n\
\
Enter (1) or (2) or (3)"
                                    )

                            if V_q == "1":
                                print("...Loading")
                                try:
                                    Video_a_1()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_a_2()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_a_3()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            Video_a_H()
                                            print("\nVideo is downloaded")
                                            break

                            elif V_q == "2":
                                print("...Loading")
                                try:
                                    Video_a_2()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_a_3()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        Video_a_H()
                                        print("\nVideo is downloaded")
                                        break

                            elif V_q == "3":
                                print("...Loading")
                                try:
                                    Video_a_3()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    Video_a_H()
                                    print("\nVideo is downloaded")
                                    break

                elif V == "2":

                    while True:

                        try:

                            ex = input(
                                "\nChoose (1) or (2):\n\
\
1- videoName.webm\n\
\
2- videoName.mp4\n"
                            )

                            if ex in ("1", "2"):

                                break

                            else:
                                raise ValueError

                        except ValueError:
                            print(
                                "\ninvalid input.\n\
\
Enter (1) or (2)\n"
                            )

                    if ex == "1":

                        while True:

                            while True:

                                try:

                                    webm = input(
                                        "\nChoose [(1) : (8)]:\n\
\
1- 2160p\n\
\
2- 1440p\n\
\
3- 1080p\n\
\
4- 720p\n\
\
5- 480p\n\
\
6- 360p\n\
\
7- 240p\n\
\
8- 144p\n"
                                    )

                                    if webm in range(1, 9):
                                        break

                                    else:
                                        raise ValueError

                                except ValueError:
                                    print(
                                        "\ninvalid input\n\
\
Enter (1) or (2) or (3) or (4) or (5) or (6) or (7) or (8)"
                                    )

                            if webm == "1":
                                print("...Loading")
                                try:
                                    Video_webm_1()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_2()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_webm_3()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_webm_4()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Video_webm_5()
                                                    print("\nVideo is downloaded")
                                                    break
                                                except:
                                                    pass
                                                    try:
                                                        Video_webm_6()
                                                        print("\nVideo is downloaded")
                                                        break
                                                    except:
                                                        pass
                                                        try:
                                                            Video_webm_7()
                                                            print(
                                                                "\nVideo is downloaded"
                                                            )
                                                            break
                                                        except:
                                                            pass
                                                            try:
                                                                Video_webm_8()
                                                                print(
                                                                    "\nVideo is downloaded"
                                                                )
                                                                break
                                                            except:
                                                                print(
                                                                    "Sorry, This Video isn't able to download without audio"
                                                                )
                                                                break

                            elif webm == "2":
                                print("...Loading")
                                try:
                                    Video_webm_2()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_3()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_webm_4()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_webm_5()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Video_webm_6()
                                                    print("\nVideo is downloaded")
                                                    break
                                                except:
                                                    pass
                                                    try:
                                                        Video_webm_7()
                                                        print("\nVideo is downloaded")
                                                        break
                                                    except:
                                                        pass
                                                        try:
                                                            Video_webm_8()
                                                            print(
                                                                "\nVideo is downloaded"
                                                            )
                                                            break
                                                        except:
                                                            print(
                                                                "Sorry, This Video isn't able to download without audio "
                                                            )
                                                            break

                            elif webm == "3":
                                print("...Loading")
                                try:
                                    Video_webm_3()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_4()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_webm_5()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_webm_6()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Video_webm_7()
                                                    print("\nVideo is downloaded")
                                                    break
                                                except:
                                                    pass
                                                    try:
                                                        Video_webm_8()
                                                        print("\nVideo is downloaded")
                                                        break
                                                    except:
                                                        print(
                                                            "Sorry, This Video isn't able to download without audio "
                                                        )
                                                        break

                            elif webm == "4":
                                print("...Loading")
                                try:
                                    Video_webm_4()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_5()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_webm_6()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_webm_7()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Video_webm_8()
                                                    print("\nVideo is downloaded")
                                                    break
                                                except:
                                                    print(
                                                        "Sorry, This Video isn't able to download without audio "
                                                    )
                                                    break

                            elif webm == "5":
                                print("...Loading")
                                try:
                                    Video_webm_5()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_6()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_webm_7()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_webm_8()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                print(
                                                    "Sorry, This Video isn't able to download without audio "
                                                )
                                                break

                            elif webm == "6":
                                print("...Loading")
                                try:
                                    Video_webm_6()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_7()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_webm_8()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            print(
                                                "Sorry, This Video isn't able to download without audio "
                                            )
                                            break

                            elif webm == "7":
                                print("...Loading")
                                try:
                                    Video_webm_7()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_webm_8()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        print(
                                            "Sorry, This Video isn't able to download without audio "
                                        )
                                        break

                            elif webm == "8":
                                print("...Loading")
                                try:
                                    Video_webm_8()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    print(
                                        "Sorry, This Video isn't able to download without audio "
                                    )
                                    break

                    elif ex == "2":

                        while True:

                            while True:

                                try:

                                    mp4 = input(
                                        "\nChoose [(1) : (6)]:\n\
\
1- 1080p\n\
\
2- 720p\n\
\
3- 480p\n\
\
4- 360p\n\
\
5- 240p\n\
\
6- 144p\n"
                                    )

                                    if mp4 in range(1, 7):
                                        break

                                    else:
                                        raise ValueError

                                except ValueError:
                                    print(
                                        "\ninvalid input\n\
\
Enter (1) or (2) or (3) or (4) or (5) or (6)"
                                    )

                            if mp4 == "1":
                                print("...Loading")
                                try:
                                    Video_mp4_1()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_mp4_2()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_mp4_3()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_mp4_4()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Video_mp4_5()
                                                    print("\nVideo is downloaded")
                                                    break
                                                except:
                                                    pass
                                                    try:
                                                        Video_mp4_6()
                                                        print("\nVideo is downloaded")
                                                        break
                                                    except:
                                                        print(
                                                            "Sorry, This Video isn't able to download without audio"
                                                        )
                                                        break

                            elif mp4 == "2":
                                print("...Loading")
                                try:
                                    Video_mp4_2()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_mp4_3()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_mp4_4()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_mp4_5()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Video_mp4_6()
                                                    print("\nVideo is downloaded")
                                                    break
                                                except:
                                                    pass
                                                    print(
                                                        "Sorry, This Video isn't able to download without audio "
                                                    )
                                                    break

                            elif mp4 == "3":
                                print("...Loading")
                                try:
                                    Video_mp4_3()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_mp4_4()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_mp4_5()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Video_mp4_6()
                                                print("\nVideo is downloaded")
                                                break
                                            except:
                                                pass
                                                print(
                                                    "Sorry, This Video isn't able to download without audio "
                                                )
                                                break

                            elif mp4 == "4":
                                print("...Loading")
                                try:
                                    Video_mp4_4()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_mp4_5()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Video_mp4_6()
                                            print("\nVideo is downloaded")
                                            break
                                        except:
                                            pass
                                            print(
                                                "Sorry, This Video isn't able to download without audio "
                                            )
                                            break

                            elif mp4 == "5":
                                print("...Loading")
                                try:
                                    Video_mp4_5()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Video_mp4_6()
                                        print("\nVideo is downloaded")
                                        break
                                    except:
                                        pass
                                        print(
                                            "Sorry, This Video isn't able to download without audio "
                                        )
                                        break

                            elif mp4 == "6":
                                print("...Loading")
                                try:
                                    Video_mp4_6()
                                    print("\nVideo is downloaded")
                                    break
                                except:
                                    pass
                                    print(
                                        "Sorry, This Video isn't able to download without audio "
                                    )
                                    break

                break

        elif V_A == "2":

            while True:

                while True:

                    try:

                        A = input(
                            "\nChoose (1) or (2):\n\
\
1- High Volume\n\
\
2- Custom\n"
                        )

                        if A in ("1", "2"):
                            break

                        else:
                            raise ValueError

                    except ValueError:
                        print(
                            "\ninvalid input.\n\
\
Please enter (1) or (2)"
                        )

                while True:

                    if A == "1":
                        print("...Loading")
                        Audio_H()
                        print("\nAudio is downloaded")
                        break

                    elif A == "2":

                        while True:

                            try:

                                A_q = input(
                                    "\nChoose [(1) : (5)]\n\
1- 160k\n\
\
2- 128k\n\
\
3- 70k\n\
\
4- 50k\n\
\
5- 48k\n"
                                )

                                if A_q in ("1", "2", "3", "4", "5"):
                                    break

                                else:
                                    raise ValueError

                            except ValueError:
                                print(
                                    "\ninvalid input.\n\
\
Enter (1) or (2) or (3) or (4) or (5)"
                                )

                        while True:

                            if A_q == "1":
                                print("...Loading")
                                try:
                                    Audio_1()
                                    print("\nAudio is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Audio_2()
                                        print("\nAudio is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Audio_3()
                                            print("\nAudio is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Audio_4()
                                                print("\nAudio is downloaded")
                                                break
                                            except:
                                                pass
                                                try:
                                                    Audio_5()
                                                    print("\nAudio is downloaded")
                                                    break
                                                except:
                                                    print(
                                                        "Sorry, This Video isn't able to download audio only"
                                                    )
                                                    break

                            elif A_q == "2":
                                print("...Loading")
                                try:
                                    Audio_2()
                                    print("\nAudio is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Audio_3()
                                        print("\nAudio is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Audio_4()
                                            print("\nAudio is downloaded")
                                            break
                                        except:
                                            pass
                                            try:
                                                Audio_5()
                                                print("\nAudio is downloaded")
                                                break
                                            except:
                                                print(
                                                    "Sorry, This Video isn't able to download audio only"
                                                )
                                                break

                            elif A_q == "3":
                                print("...Loading")
                                try:
                                    Audio_3()
                                    print("\nAudio is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Audio_4()
                                        print("\nAudio is downloaded")
                                        break
                                    except:
                                        pass
                                        try:
                                            Audio_5()
                                            print("\nAudio is downloaded")
                                            break
                                        except:
                                            print(
                                                "Sorry, This Video isn't able to download audio only"
                                            )
                                            break

                            elif A_q == "4":
                                print("...Loading")
                                try:
                                    Audio_4()
                                    print("\nAudio is downloaded")
                                    break
                                except:
                                    pass
                                    try:
                                        Audio_5()
                                        print("\nAudio is downloaded")
                                        break
                                    except:
                                        print(
                                            "Sorry, This Video isn't able to download audio only"
                                        )
                                        break

                            elif A_q == "5":
                                try:
                                    Audio_5()
                                    print("\nAudio is downloaded")
                                    break
                                except:
                                    print(
                                        "Sorry, This Video isn't able to download audio only"
                                    )
                                    break

                            break

                break

        print("\nWe are happy about that\n")
        break

    while True:

        try:

            repeat = input("Do you want to download another video/audio? (y/n):\n")

            if repeat in ("y", "Y", "n", "N"):
                break

            else:
                raise ValueError

        except ValueError:
            print("\ninvalid input. please enter y, n\n")

    if repeat in ("y", "Y"):
        print("\nWe are happy about that\n")

    elif repeat in ("n", "N"):
        print("\nWe hope have made you happy\n")
        input("Press 'enter' to exit\n")
        break
