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
        #self.onStopped() #activate the output of the box
        session = self.session()
        motion_service = session.service("ALMotion")

        motion_service.setStiffnesses("RArm", 1.0)
        release_speed = self.getParameter("releaseSpeed")
        self.logger.info("release speed:" + release_speed)
        if release_speed == "slow":
            motion_service.angleInterpolationWithSpeed("RHand",1,0.05)
            time.sleep(2.0)
        elif release_speed == "fast":
            motion_service.angleInterpolationWithSpeed("RHand",1,0.5)
            time.sleep(2.0)
        else:
            self.logger.info("release speed : wrong input")
            motion_service.angleInterpolationWithSpeed("RHand",1,0.1)
            time.sleep(2.0)

        motion_service.setStiffnesses("RArm", 0.0)

        self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
