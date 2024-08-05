/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

#include "MY_LIS3DSH.h"

/* USER CODE END Includes */

/* USER CODE BEGIN PV */

LIS3DSH_DataScaled myData;
uint8_t drdyFlag=0;

/* USER CODE END PV */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
  /* Prevent unused argument(s) compilation warning */
  UNUSED(GPIO_Pin);
  /* NOTE: This function Should not be modified, when the callback is needed,
           the HAL_GPIO_EXTI_Callback could be implemented in the user file
   */

  drdyFlag = 1;
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  // .....

  /* USER CODE BEGIN 2 */

  LIS3DSH_InitTypeDef myAccConfigDef;

  myAccConfigDef.dataRate = LIS3DSH_DATARATE_25;
  myAccConfigDef.fullScale = LIS3DSH_FULLSCALE_4;
  myAccConfigDef.antiAliasingBW = LIS3DSH_FILTER_BW_50;
  myAccConfigDef.enableAxes = LIS3DSH_XYZ_ENABLE;
  myAccConfigDef.interruptEnable = true;
  LIS3DSH_Init(&hspi1, &myAccConfigDef);

  LIS3DSH_X_calibrate(-1000.0, 980.0);
  LIS3DSH_Y_calibrate(-1020.0, 1040.0);
  LIS3DSH_Z_calibrate(-920.0, 1040.0);

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
	  if(drdyFlag == 1)
	  {
		  myData = LIS3DSH_GetDataScaled();
		  drdyFlag = 0;
	  }
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}
