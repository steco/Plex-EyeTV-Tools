import Media, plistlib, re

recdSuffix  = ".eyetv"
metaSuffix  = ".eyetvp"
liveSuffix  = "Live TV Buffer.eyetv"
videoSuffix = ".mpg"  # Use .m4v if you needed

def ScanTVShow(path, files, mediaList, subdirs):
    """Scans the path for an EyeTV recording of the given genre.
   
    An EyeTV recording consists of the actual video file(s) and a set
    of metadata files.  First makes sure that the given files do exist.
    Then inspect the metadata to see if the recording belongs to the
    desired genre.

    """
    if len(files) < 1:
        return
    if path.endswith(recdSuffix) and not path.endswith(liveSuffix):
      recording = None
      metadata  = None

      for file in files:
        if file.endswith(videoSuffix):
            recording = file
        if file.endswith(metaSuffix):
            metadata  = file
        if recording and metadata:
            break

      if recording and metadata:
        metadataPList = plistlib.readPlist(metadata)

        title = lookupPlist(metadataPList, 'epg info', 'TITLE')
        abstract = lookupPlist(metadataPList, 'epg info', 'ABSTRACT')
        findEpisode = re.search('(\d+)\/.*', abstract)
        episode = ""
        if findEpisode:
          episode = findEpisode.group(1)

        print abstract
        print "Found " + title + ", episode " + episode
        episode = Media.Episode(title, "1", episode, abstract)
        episode.parts.append(recording)
        mediaList.append(episode)

def ScanMovie(path, files, mediaList, subdirs):
    """Scans the path for an EyeTV recording of the given genre.

    
    An EyeTV recording consists of the actual video file(s) and a set
    of metadata files.  First makes sure that the given files do exist.
    Then inspect the metadata to see if the recording belongs to the
    desired genre.

    """
    if len(files) < 1:
        return
    if path.endswith(recdSuffix) and not path.endswith(liveSuffix):
      recording = None
      metadata  = None

      for file in files:
        if file.endswith(videoSuffix):
            recording = file
        if file.endswith(metaSuffix):
            metadata  = file
        if recording and metadata:
            break

      if recording and metadata:
        metadataPList = plistlib.readPlist(metadata)

        title = lookupPlist(metadataPList, 'epg info', 'TITLE')
        abstract = lookupPlist(metadataPList, 'epg info', 'ABSTRACT')
        findYear = re.search('.*((19|20)\d{2}).*', abstract)
        year = ""
        if findYear:
          year = findYear.group(1)
 
        print "Found " + title + ", year " + year
        movie = Media.Movie(title, year)
        movie.parts.append(recording)
        mediaList.append(movie)

def lookupPlist(plist, *args):
    for key in args:
        try:
            plist = plist[key]
        except KeyError:
            return None
    return plist

                        
