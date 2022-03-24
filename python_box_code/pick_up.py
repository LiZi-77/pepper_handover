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

        # 1.go to the start posture
        self.logger.info("Start to stand still")
        posture_service = session.service("ALRobotPosture")
        posture_service.goToPosture("StandInit",0.2)
        time.sleep(3.0)

        # 2.pick up something
        self.logger.info("Start to pick up something")
        motion_service = session.service("ALMotion")
        motion_service.setStiffnesses("Head", 1.0)
        motion_service.setStiffnesses("RArm", 1.0)

        names            = ["HeadYaw","HeadPitch","RElbowRoll","RShoulderPitch","RElbowYaw","RShoulderRoll"]
        angles           = [-45.0*almath.TO_RAD,5.0*almath.TO_RAD,50.0*almath.TO_RAD,70.0*almath.TO_RAD,100.0*almath.TO_RAD,-60.0*almath.TO_RAD]
        fractionMaxSpeed = [0.05]*6

        motion_service.setAngles(names,angles,fractionMaxSpeed)

        time.sleep(4.0)
        motion_service.angleInterpolationWithSpeed("RHand",0,0.1)


        self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
