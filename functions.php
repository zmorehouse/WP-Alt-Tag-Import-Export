<?php
// Append this to your functions.php - run once then remove. 

function update_image_alt_tags_from_csv() {
    $csv_file = ABSPATH . 'wp-content/path/image_alt_tags.csv'; // Path to your CSV

    if (!file_exists($csv_file)) {
        error_log('CSV file not found.');
        return;
    }

    if (($handle = fopen($csv_file, 'r')) !== false) {
        $row = 0;

        while (($data = fgetcsv($handle, 1000, ',')) !== false) {
            $row++;

            if ($row == 1) continue;

            $title = trim($data[0]); 
            $alt_text = trim($data[1]); 

            error_log("Processing: $title with alt text: $alt_text");

            // Match attachment by title
            global $wpdb;
            $attachment_id = $wpdb->get_var($wpdb->prepare(
                "SELECT ID FROM $wpdb->posts WHERE post_type = 'attachment' AND post_title = %s",
                $title
            ));

            // If we found the attachment, update its alt text
            if ($attachment_id) {
                update_post_meta($attachment_id, '_wp_attachment_image_alt', sanitize_text_field($alt_text));
                error_log("Updated alt text for: $title (ID: $attachment_id)");
            } else {
                error_log("No exact match found for: $title");
            }
        }
        fclose($handle);
    }
}

add_action('admin_init', 'update_image_alt_tags_from_csv');
?>
