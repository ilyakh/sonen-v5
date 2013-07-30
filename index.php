<?php get_header(); ?>

    <!-- container -->

    <?php
        $posts_array = get_posts( $args );
        print( count( $posts_array ) );
    ?>

    <!-- /container -->

<?php get_footer(); ?>