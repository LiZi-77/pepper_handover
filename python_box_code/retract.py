class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)


    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        import almath
        session = self.session()
        motion_service = session.service("ALMotion")
        rs =1.0#default speed
        retractionSpeed = self.getParameter("retractionSpeed")
        self.logger.info("retraction speed : " + retractionSpeed)
        if retractionSpeed == "slow":
            rs = 0.05
        elif retractionSpeed == "fast":
            rs = 0.5
        else:
            self.logger.info("retratcion speed : wrong input")


        # 4.Retract Hand Mid
        retractionAngle = self.getParameter("retractionAngle")
        motion_service.setStiffnesses("RArm", 1.0)
        if retractionAngle == "mode 1":
            self.logger.info("4.Retraction mode 1")

            #motion_service.setAngles("RElbowRoll",0.5*almath.TO_RAD,rs)
            #names            = ["RElbowRoll","RShoulderPitch","RElbowYaw","RShoulderRoll"]
            #angles           = [5.0*almath.TO_RAD, 40.0*almath.TO_RAD, 100.0*almath.TO_RAD, -5.0*almath.TO_RAD]
        #fractionMaxSpeed = [rs]*4
        #motion_service.setAngles(names,angles,fractionMaxSpeed)
            #names            = ["RElbowRoll","RShoulderPitch","RElbowYaw","RShoulderRoll"]
            #angles           = [5.0*almath.TO_RAD,40.0*almath.TO_RAD,100.0*almath.TO_RAD,-20.0*almath.TO_RAD]
            #fractionMaxSpeed = [rs]*4

            #motion_service.setAngles(names,angles,fractionMaxSpeed)
            motion_service.setAngles(["RShoulderPitch","RElbowRoll","RShoulderRoll"],[95.0*almath.TO_RAD,30.0*almath.TO_RAD,-20.0*almath.TO_RAD],[rs]*3)
        elif retractionAngle == "mode 2":
            self.logger.info("4.Retraction mode 2")
            #motion_service.setAngles("RShoulderPitch",95.0*almath.TO_RAD,rs)
            motion_service.setAngles(["RShoulderPitch","RElbowRoll"],[95.0*almath.TO_RAD,30.0*almath.TO_RAD],[rs]*2)
        else:
            self.logger.info("retraction angle : wrong input")
             #default
            self.logger.info("4.Retraction default mode 1")
            motion_service.setAngles("RElbowRoll",5.0*almath.TO_RAD,rs)

        time.sleep(2.0)
        motion_service.setStiffnesses("RArm", 0.0)

        # 5.Back to stand Pos
        #self.logger.info("5.Back to stand still")
        #posture_service = session.service("ALRobotPosture")
        #posture_service.goToPosture("Stand",rs)
        #time.sleep(3.0)

        self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
