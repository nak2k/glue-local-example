FROM amazon/aws-glue-libs:glue_libs_4.0.0_image_01

RUN unzip /home/glue_user/aws-glue-libs/PyGlue.zip -d /home/glue_user/aws-glue-libs/PyGlue && \
    sed -ibak -e 's/PyGlue.zip/PyGlue/' /home/glue_user/.bashrc
