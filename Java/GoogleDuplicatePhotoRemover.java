import java.util.HashMap;
import java.io.File;
/** 
 * Written by Ryan D'souza 
 * When downloading a photo library from Google Photos, Google includes two copies of each photo: the raw picture and an edited - enhanced - photo.
 * "rsync -av *'/' All\ Photos" in the terminal 
    gets all the photos from the folders (day1/photo1_1, day1/photo1_2, day2/photo2_1, day2/photo2_2) and 
    moves them to a single directory (allPhotos/photo1_1, allPhotos/photo1_2, allPhotos/photos2_1, allPhotos/photos2_2)
 * The raw and edited-photo versions take use significant memory and causes duplicates 
    when just viewing the files ie.- photo1_1.jpg photo1_1-edited.jpg, photo2_1.jpg photo2_2-edited.jpg
 * This program looks through all the photos in a directory and, if there is an edited version, deletes the original. 
 * If there is no edited version, the program does nothing*/

public class GoogleDuplicatePhotoRemover {

    public static void main(String[] ryan) throws Exception {

        //For fun statistics
        int numPhotosDeleted = 0;
        long bytesDeleted = 0;
        
        //To hold all the file names
        final HashMap<String, String> fileNames = new HashMap<String, String>();

        //All the files in the directory this program is run from
        final File folderWithAllFiles = new File(System.getProperty("user.dir"));
        final File[] allFiles = folderWithAllFiles.listFiles();

        //Go through all the files
        for(File file : allFiles) { 
            if(file.isFile()) {

                //Just the file name without the extension
                final String newFileName = file.getName().replace(".jpg", "").replace(".png", "").replace(".jpeg", "")
                                    .replace(".3gp", "").replace(".gif", "").replace(".mov", "").replace(".mp4", "");

                //Add it to our set of names
                fileNames.put(newFileName, file.getName());
            }
        }

        //Go through all of our names
        for(String file : fileNames.keySet()) {

            //If there is an edited version in the directory
            if(fileNames.containsKey(file + "-edited")) {

                //Get the original
                final File toDelete = new File(fileNames.get(file));
                
                //Update the stats
                numPhotosDeleted++;
                bytesDeleted += toDelete.length();

                //And delete the original, keeping the edited version
                if(toDelete.delete()) {
                    System.out.println("Deleted: " + file);
                }
                else {
                    System.out.println("Problem deleting: " + file);
                }
            }
        }

        System.out.println("NUM DELETED FILES: " + numPhotosDeleted);

        final double MBDeleted = bytesDeleted / Math.pow(1024, 2);

        System.out.println("MBDELETED: " + MBDeleted + "\tBYTES DELETED: " + bytesDeleted);
    }
}
