import java.util.*;

public class Example {

    public static void main(String[] args) {
        String password = "aaaa";
        String password1 = "";
        String URL_FORMAT = "sftp://%s:%s@%s:%d/%s";
        // ruleid: ftp
        String connectionString = String.format(URL_FORMAT, username, password, host, database, options);
        // ruleid: ftp
        String connectionString1 = String.format("ftp://superusername:%s@%s/%s?%s",password, host, database, options);
        // ok: ftp
        String connectionString = String.format("ftp://superusername:%s@%s/%s?%s",a,password, host, database, options);
        // ok: ftp
        String connectionString1 = String.format("ftp://superusername:%s@%s/%s?%s",password1, host, database, options);
    }
}
