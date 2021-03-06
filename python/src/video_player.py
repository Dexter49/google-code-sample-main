"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_playing_video = None

    def sort_videos_by_title(self, video):
        return video.title

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        videos = self._video_library.get_all_videos()

        videos.sort(key = self.sort_videos_by_title)

        print("Here's a list of all available videos")

        for video in videos:
            print(f"\t {video.title}, ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

    def stop_video(self):
        """Stops the current video."""

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        search_term = search_term.lower()
        all_videos = self._video_library.get_all_videos()
        found = []
        for video in all_videos:
            if search_term in video.title.lower():
                found.append(video)
        if len(found) >= 1:
            print('Here are the results for '+ search_term + ':')
            idx = 1
            for video in found:
                tags = ' [' + video.tags[0] + ' ' + video.tags[1] + ']'
                ids = '(' + video.video_id + ')'
                print(f'    {idx}) '+ video.title + ' ' + ids + tags)
                idx += 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            try:
                self.play_video(found[int(answer)-1].video_id)
            except ValueError:
                pass
            except IndexError:
                pass
        else:
            print('No search results for', search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        found = []
        for video in all_videos:
            if video_tag in video.tags:
                found.append(video)
        if len(found) >= 1:
            print('Here are the results for '+ video_tag + ':')
            idx = 1
            for video in found:
                tags = ' [' + video.tags[0] + ' ' + video.tags[1] + ']'
                ids = '(' + video.video_id + ')'
                print(f'    {idx}) '+ video.title + ' ' + ids + tags)
                idx += 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            try:
                self.play_video(found[int(answer)-1].video_id)
            except ValueError:
                pass
            except IndexError:
                pass
        else:
            print('No search results for', video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
